import asyncio

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext

from data.YeezyAPI import YeezyAPI
from data.constants import REQUEST_LIMIT_SECONDS
from data.repositories.accesses import AccessRepository
from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.transaction_rep.account_transaction import AccountTransactionRepository
from domain.middlewares.MCCLimitClient import MCCLimitClientMiddleware
from domain.notification.admin_notify import NotificationAdmin
from domain.states.client.account.CreateAccountClientState import CreateAccountClientState
from presentation.keyboards.client.kb_mcc.kb_accounts import CreateSubAccountClient, kb_back_detail_mcc

router = Router()

router.message.middleware(MCCLimitClientMiddleware())
router.callback_query.middleware(MCCLimitClientMiddleware())

create_account_last_call_times = []


async def remove_limiter(team_uuid):
    """Видалення ліміту через 5 секунди."""
    print(f"create_account List block request before {create_account_last_call_times}")
    print(f"create_account team remove block {team_uuid}")
    await asyncio.sleep(REQUEST_LIMIT_SECONDS)
    create_account_last_call_times.remove(team_uuid)  # Видаляємо ключ, якщо існує
    print(f"create_account List block request after {create_account_last_call_times}")


@router.callback_query(CreateSubAccountClient.filter())
async def create_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(CreateAccountClientState.Name)
    await callback.message.edit_text(i18n.CLIENT.ACCOUNT.CREATE.NAME(), reply_markup=kb_back_detail_mcc)


@router.message(CreateAccountClientState.Name)
async def create_name_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    if len(message.text) > 255:
        await message.answer(
            i18n.CLIENT.ACCOUNT.CREATE.NAME.ERROR(len=len(message.text)), reply_markup=kb_back_detail_mcc)
        return

    await state.update_data(name=message.text)
    await state.set_state(CreateAccountClientState.Email)
    await message.answer(i18n.CLIENT.ACCOUNT.CREATE.EMAIL(), reply_markup=kb_back_detail_mcc)


@router.message(CreateAccountClientState.Email)
async def create_email_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    from domain.handler.client.mcc.accounts.change_email_account_client import is_valid_email
    if not is_valid_email(message.text):
        await message.answer(i18n.CLIENT.ACCOUNT.CHANGE_EMAIL.ERROR(), reply_markup=kb_back_detail_mcc)
        return

    await state.update_data(email=message.text)
    await state.set_state(CreateAccountClientState.Amount)
    await message.answer(i18n.CLIENT.ACCOUNT.CREATE.AMOUNT(), reply_markup=kb_back_detail_mcc)


@router.message(CreateAccountClientState.Amount)
async def create_amount_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    try:
        topup_value = int(message.text)
        if topup_value < 100 or topup_value > 10000:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.CLIENT.ACCOUNT.TOPUP.VALUE.ERROR(), reply_markup=kb_back_detail_mcc)
        return

    await state.update_data(amount=topup_value)
    await state.set_state(CreateAccountClientState.Timezone)
    await message.answer(i18n.CLIENT.ACCOUNT.CREATE.TIMEZONE(), reply_markup=kb_back_detail_mcc)


@router.message(CreateAccountClientState.Timezone)
async def create_timezone_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    try:
        timezone = int(message.text)
        if timezone < -12 or timezone > +14:
            raise ValueError

        timezone = f"UTC+{timezone}" if timezone >= 0 else f"UTC-{timezone * -1}"
    except ValueError as e:
        await message.answer(i18n.CLIENT.ACCOUNT.CREATE.TIMEZONE.ERROR(), reply_markup=kb_back_detail_mcc)
        return

    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    access = AccessRepository().access_by_user_id(message.from_user.id)

    print(f"create_timezone_save access {access}")
    print(f"create_timezone_save balance {BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])}")

    # Перевіряємо, чи вже був запит
    team_uuid = access['team_uuid']
    if team_uuid in create_account_last_call_times:
        print(f"create_timezone_save List block if reject request {create_account_last_call_times}")
        print(f"create_timezone_save team uuid if reject request {access['team_name']}")
        await message.answer(i18n.CLIENT.WAIT_FOR_REQUEST())
        return

    # Встановлюємо обмеження на запит
    create_account_last_call_times.append(team_uuid)

    # обнуляємо стан FSM
    await state.set_state(None)

    # check value balance
    balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])
    if balance['balance'] < data['amount']:
        await message.answer(i18n.CLIENT.ACCOUNT.CREATE.AMOUNT.NOMONEY(balance=balance['balance']),
                             reply_markup=kb_back_detail_mcc)
        return

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await message.edit_text(i18n.MCC.AUTH.FAIL(
            mcc_name=mcc['mcc_name']),
            reply_markup=kb_back_detail_mcc
        )
        return

    # create account by API
    def create_account_api():
        return YeezyAPI().create_account(auth['token'], data['email'], data['amount'], timezone)

    create_account_transaction = AccountTransactionRepository().create_account_transaction(
        data, create_account_api, timezone
    )

    asyncio.create_task(remove_limiter(team_uuid))

    # transaction create account
    if not create_account_transaction['result']:
        await message.answer(i18n.CLIENT.ACCOUNT.CREATE.FAIL(), reply_markup=kb_back_detail_mcc)
        await NotificationAdmin.user_create_account_error(message.from_user.id, bot, i18n, data,
                                                          create_account_transaction['error'])
        return

    # All creation account success
    await message.answer(i18n.CLIENT.ACCOUNT.CREATE.SUCCESS(
        mcc_name=mcc['mcc_name']), reply_markup=kb_back_detail_mcc
    )
    await NotificationAdmin.user_create_account(
        message.from_user.id, bot, i18n, data, create_account_transaction['account_uid']
    )
