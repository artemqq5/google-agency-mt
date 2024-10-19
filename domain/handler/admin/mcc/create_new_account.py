from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.YeezyAPI import YeezyAPI
from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.teams import TeamRepository
from data.repositories.transaction_rep.account_transaction import AccountTransactionRepository
from domain.notification.admin_notify import NotificationAdmin
from domain.states.admin.account.CreateAccountAdminState import CreateAccountAdminState
from presentation.keyboards.admin.kb_mcc.kb_accounts import SwitchGeneralMCC, CreateSubAccountAdmin, \
    kb_back_detail_mcc_admin, kb_team_uuid_skip_admin, SkipTeamUUIDAccountCreate

router = Router()


@router.callback_query(CreateSubAccountAdmin.filter())
async def create_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(CreateAccountAdminState.Name)
    await callback.message.edit_text(i18n.ADMIN.ACCOUNT.CREATE.NAME(), reply_markup=kb_back_detail_mcc_admin)


@router.message(CreateAccountAdminState.Name)
async def create_name_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    if len(message.text) > 255:
        await message.answer(
            i18n.ADMIN.ACCOUNT.CREATE.NAME.ERROR(len=len(message.text)), reply_markup=kb_back_detail_mcc_admin)
        return

    await state.update_data(name=message.text)
    await state.set_state(CreateAccountAdminState.TeamUUID)
    await message.answer(i18n.ADMIN.ACCOUNT.CREATE.TEAM(), reply_markup=kb_team_uuid_skip_admin)


@router.message(CreateAccountAdminState.TeamUUID)
async def create_team_uuid_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    input_team_uuid = message.text
    team = TeamRepository().team_by_uuid(input_team_uuid)

    if not team:
        await message.answer(i18n.ADMIN.ACCOUNT.CREATE.TEAM.ERROR(), reply_markup=kb_team_uuid_skip_admin)
        return

    await state.update_data(team_uuid=input_team_uuid)
    await state.set_state(CreateAccountAdminState.Email)
    await message.answer(
        i18n.ADMIN.ACCOUNT.CREATE.EMAIL.TEAM_CHOICED(team_name=team['team_name']),
        reply_markup=kb_back_detail_mcc_admin
    )


@router.callback_query(SkipTeamUUIDAccountCreate.filter(), CreateAccountAdminState.TeamUUID)
async def create_team_uuid_skip(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(CreateAccountAdminState.Email)
    await callback.message.edit_text(i18n.ADMIN.ACCOUNT.CREATE.EMAIL.TEAM_SKIP(), reply_markup=kb_back_detail_mcc_admin)


@router.message(CreateAccountAdminState.Email)
async def create_email_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    from domain.handler.client.mcc.accounts.change_email_account_client import is_valid_email
    if not is_valid_email(message.text):
        await message.answer(i18n.ADMIN.ACCOUNT.CHANGE_EMAIL.ERROR(), reply_markup=kb_back_detail_mcc_admin)
        return

    await state.update_data(email=message.text)
    await state.set_state(CreateAccountAdminState.Amount)
    await message.answer(i18n.ADMIN.ACCOUNT.CREATE.AMOUNT(), reply_markup=kb_back_detail_mcc_admin)


@router.message(CreateAccountAdminState.Amount)
async def create_amount_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    try:
        topup_value = int(message.text)
        if topup_value < 50 or topup_value > 10000:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.ADMIN.ACCOUNT.TOPUP.VALUE.ERROR(), reply_markup=kb_back_detail_mcc_admin)
        return

    await state.update_data(amount=topup_value)
    await state.set_state(CreateAccountAdminState.Timezone)
    await message.answer(i18n.ADMIN.ACCOUNT.CREATE.TIMEZONE(), reply_markup=kb_back_detail_mcc_admin)


@router.message(CreateAccountAdminState.Timezone)
async def create_timezone_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    try:
        timezone = int(message.text)
        if timezone < -12 or timezone > +14:
            raise ValueError

        timezone = f"UTC+{timezone}" if timezone >= 0 else f"UTC-{timezone * -1}"
    except ValueError as e:
        await message.answer(i18n.ADMIN.ACCOUNT.CREATE.TIMEZONE.ERROR(), reply_markup=kb_back_detail_mcc_admin)
        return

    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await message.edit_text(i18n.MCC.AUTH.FAIL(
            mcc_name=mcc['mcc_name']),
            reply_markup=kb_back_detail_mcc_admin
        )
        return

    # create account by API
    def create_account_api():
        return YeezyAPI().create_account(auth['token'], data['email'], data['amount'], timezone)

    create_account_transaction = AccountTransactionRepository().create_account_transaction_admin(
        data, create_account_api, timezone
    )

    # transaction create account
    if not create_account_transaction['result']:
        await message.answer(
            i18n.FAIL.ACCOUNT.CREATE.FAIL(error=create_account_transaction['error']),
            reply_markup=kb_back_detail_mcc_admin
        )
        return

    # All creation account success
    await message.answer(i18n.CLIENT.ACCOUNT.CREATE.SUCCESS(
        mcc_name=mcc['mcc_name']), reply_markup=kb_back_detail_mcc_admin
    )
