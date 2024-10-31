import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor

from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramNetworkError
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.YeezyAPI import YeezyAPI
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from presentation.keyboards.admin.kb_specific.kb_specific import kb_specific_back, kb_load_account_confirmation, \
    SpecificLoadAccounts, SpecificLoadAccountsConfirmation, kb_specific_choice_mcc, SpecificChoiceMCC, \
    SpecificChoiceMCC_Navigation

router = Router()


@router.callback_query(SpecificLoadAccounts.filter())
async def load_accounts_choice(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    mccs = MCCRepository().mccs()
    await callback.message.edit_text(
        i18n.ADMIN.SPECIFIC.LOAD.CHOICE_MCC(),
        reply_markup=kb_specific_choice_mcc(mccs)
    )


@router.callback_query(SpecificChoiceMCC_Navigation.filter())
async def load_accounts_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])

    mccs = MCCRepository().mccs()
    await callback.message.edit_text(
        i18n.ADMIN.SPECIFIC.LOAD.CHOICE_MCC(),
        reply_markup=kb_specific_choice_mcc(mccs, current_page=page)
    )


@router.callback_query(SpecificChoiceMCC.filter())
async def load_accounts_(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = callback.data.split(":")[1]
    print(data)
    await state.update_data(mcc_uuid=data)
    await callback.message.edit_text(i18n.ADMIN.SPECIFIC.LOAD.WARNING(), reply_markup=kb_load_account_confirmation)


@router.callback_query(SpecificLoadAccountsConfirmation.filter())
async def load_accounts_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    mcc_accounts = 0
    all_accounts = 0
    result = ""
    account_already_checked = 0  # Переносимо змінну в загальну функцію

    await callback.message.delete()
    await callback.message.answer(i18n.ADMIN.SPECIFIC.LOAD.PROCESSING())

    # Використовуємо ThreadPoolExecutor для багатопоточності
    executor = ThreadPoolExecutor(max_workers=5)  # Наприклад, 3 потоки
    lock = asyncio.Lock()  # Створюємо блокування для синхронізації доступу до змінної

    async def process_page(mcc_item, auth_token, page_number, message_id, total_pages):
        page_counts = 0

        # Виконуємо запит у потоці
        loop = asyncio.get_running_loop()
        page_response = await loop.run_in_executor(executor, YeezyAPI().get_verify_accounts, auth_token, page_number, 1000)

        current_page_accounts = [acc for acc in page_response.get('accounts', []) if
                                 acc['status'] in ('ACTIVE', 'RESTORED')]
        page_accounts_count_check = len(page_response.get('accounts', []))

        for account in current_page_accounts:
            if not SubAccountRepository().account_by_uid(account['uid']):
                if not SubAccountRepository().add(
                        account_uid=account['uid'],
                        mcc_uuid=mcc_item['mcc_uuid'],
                        account_name="None",
                        account_email=account['email'],
                        account_timezone="None",
                        team_uuid="default",
                        team_name="default"
                ):
                    await callback.message.answer(i18n.ADMIN.SPECIFIC.LOAD.FAIL(
                        email=account['email'], mcc_name=mcc_item['mcc_name']
                    ))
                    continue
                page_counts += 1

        # Синхронізовано оновлюємо змінну account_already_checked
        async with lock:
            nonlocal account_already_checked
            nonlocal mcc_accounts
            account_already_checked += page_accounts_count_check  # Оновлюємо рахунок акаунтів
            mcc_accounts += page_counts

        # Оновлюємо повідомлення кожні 5 сторінок або на останній сторінці
        if page_number % 5 == 0 or page_number == total_pages:
            await edit_message_with_retry(
                bot, callback.message.chat.id, message_id, i18n.ADMIN.SPECIFIC.LOAD.PART(
                    mcc_name=mcc_item['mcc_name'],
                    new_accounts=mcc_accounts,
                    all_accounts=page_response.get('total', '-'),
                    current_accounts=account_already_checked
                )
            )

    # Try to authenticate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.edit_text(i18n.MCC.AUTH.FAIL(
            mcc_name=mcc['mcc_name']),
            reply_markup=kb_specific_back
        )
        return

    # Get first page to determine the total number of pages
    first_page_response = YeezyAPI().get_verify_accounts(auth['token'], page=0, limit=1000)
    last_page = first_page_response.get('last_page', 1)

    # Відправляємо повідомлення про першу сторінку
    message = await callback.message.answer(i18n.ADMIN.SPECIFIC.LOAD.PART(
        mcc_name=mcc['mcc_name'],
        new_accounts=mcc_accounts,
        all_accounts=first_page_response.get('total', '-'),
        current_accounts=account_already_checked
    ))

    # Виконуємо запити для інших сторінок паралельно
    tasks = []
    for page in range(1, last_page + 1):
        task = process_page(mcc, auth['token'], page, message.message_id, last_page)
        tasks.append(task)

    await asyncio.gather(*tasks)
    result += f"{mcc['mcc_name']}: <b>{str(mcc_accounts)}</b>\n"

    all_accounts += mcc_accounts
    mcc_accounts = 0
    account_already_checked = 0

    await callback.message.answer(
        i18n.ADMIN.SPECIFIC.LOAD.RESULT(new_accounts=str(all_accounts), statistic=result))


async def edit_message_with_retry(bot, chat_id, message_id, text, retry=3):
    for attempt in range(retry):
        try:
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=text
            )
            break  # Якщо успішно, виходимо з циклу
        except TelegramNetworkError:
            logging.error("edit_message_with_retry timeout")
            if attempt < retry - 1:  # Якщо це не остання спроба
                await asyncio.sleep(5)  # Чекаємо перед наступною спробою
            else:
                raise  # Якщо остання спроба, піднімаємо помилку
