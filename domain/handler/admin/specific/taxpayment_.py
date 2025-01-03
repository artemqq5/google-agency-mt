import asyncio
import os

import pandas as pd
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, Document
from aiogram_i18n import I18nContext

from data.repositories.taxes import TaxRepository
from data.repositories.transaction_rep.tax_transaction import TaxTransactionRepository
from domain.notification.tax_client_notify import send_taxes_info_to_teams
from domain.states.admin.TaxPaymentState import TaxPaymentState
from domain.tools.send_large_message import send_large_message
from presentation.keyboards.admin.kb_specific.kb_specific import SpecificLoadTaxPayment, open_google_analytics

router = Router()
# notion_api = NotionAPI()


@router.callback_query(SpecificLoadTaxPayment.filter())
async def load_taxpayment(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(TaxPaymentState.File)
    await callback.message.answer(i18n.ADMIN.SPECIFIC.TAX.DOCUMENT())


@router.message(TaxPaymentState.File, F.document and F.document.mime_type == "text/csv")
async def taxpayment_docs(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    await state.set_state(None)

    document: Document = message.document
    file_path = f"temp_{document.file_name}"
    # Завантаження файлу
    file = await bot.download(document.file_id)
    try:
        # Зчитування CSV файлу
        with open(file_path, "wb") as f:
            f.write(file.read())

        data_dict = pd.read_csv(file_path).to_dict(orient='records')  # Перетворення в масив словників
        await check_accounts_taxes(data_dict, message, i18n, bot)

    except Exception as e:
        print(e)
        await message.answer(i18n.ADMIN.SPECIFIC.TAX.ERROR(error=str(e)))
    finally:
        os.remove(file_path)


@router.message(TaxPaymentState.File)
async def taxpayment_docs_error(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    await message.answer(i18n.ADMIN.SPECIFIC.TAX.NO_DOCUMENT())


async def check_accounts_taxes(data_dict, message, i18n, bot):
    error_count = 0
    result_data = []
    success_messages = []
    fail_messages = []

    for data in data_dict:
        try:
            result = TaxTransactionRepository().add_tax_transaction(data)
            if result['result']:
                tax_data = TaxRepository().get(result['taxID'])
                result_data.append(tax_data)
                # Додаємо повідомлення про успішну транзакцію до списку
                success_messages.append(i18n.ADMIN.SPECIFIC.TAX.SUCCESS(
                    client_link=tax_data['client_link'], mcc_name=result['mcc_name'], team=tax_data['team_name'],
                    amount=tax_data['amount'],
                    currency=tax_data['currency'], status=tax_data['status'], email=tax_data['email'],
                    desc=tax_data['desc'], date=str(tax_data['date'])
                ))
            else:
                raise Exception(result['error'])
        except Exception as e:
            error_count += 1
            print(e)
            # Додаємо повідомлення про помилку до списку
            fail_messages.append(i18n.ADMIN.SPECIFIC.TAX.FAIL(email=data['Google email'], error=str(e)))

    # Відправляємо всі успішні повідомлення
    await send_large_message(message, "\n\n".join(success_messages))

    # Відправляємо всі повідомлення про помилки
    await send_large_message(message, "\n\n".join(fail_messages))

    # Додавання всіх успішних транзакцій до notion
    # for tax in result_data:
    #     await notion_api.add_to_notion(tax)

    # Відправляємо підсумкове повідомлення
    await message.answer(i18n.ADMIN.SPECIFIC.TAX.SUMMARY(
        taxes_count=len(data_dict),
        taxes_success=len(data_dict) - error_count,
        taxes_fail=error_count
    ), reply_markup=open_google_analytics)

    await send_taxes_info_to_teams(result_data, bot, message, i18n)
