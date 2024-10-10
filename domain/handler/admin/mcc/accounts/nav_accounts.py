from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.YeezyAPI import YeezyAPI
from data.constants import ADMIN
from data.repositories.accesses import AccessRepository
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountMCC
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.handler.admin.mcc import add_new_mcc
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_mcc.kb_accounts import *

router = Router()

# router.include_routers(
# )


@router.callback_query(BackAccountsManage.filter())
async def accounts_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    accounts = SubAccountMCC().accounts_by_mcc_uuid(data['mcc_uuid'])

    await callback.message.edit_text(text=i18n.ADMIN.MCC(), reply_markup=kb_accounts_manage(accounts, data.get('last_page_accounts', 1)))


@router.callback_query(NavigationAccount.filter())
async def accounts_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()

    accounts = SubAccountMCC().accounts_by_mcc_uuid(data['mcc_uuid'])

    await state.update_data(last_page_accounts=page)

    await callback.message.edit_reply_markup(reply_markup=kb_accounts_manage(accounts, page))


@router.callback_query(ShowDetailAccount.filter())
async def account_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    account_uid = callback.data.split(":")[1]
    account = SubAccountMCC().account_by_uid(account_uid)
    team = TeamRepository().team_by_uuid(account['team_uuid'])
    mcc = MCCRepository().mcc_by_uuid(account['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.answer(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    # Get Account API info
    account_api_response = YeezyAPI().get_verify_account(auth['token'], account_uid)
    account_api = account_api_response.get('accounts', [{}])[0]

    await state.update_data(account_uid=account_uid)

    await callback.message.edit_text(
        text=i18n.ACCOUNTS.DETAIL(
            name=account['account_name'],
            mcc_name=mcc['mcc_name'],
            status=account_api.get('status', 'no info'),
            email=account['account_email'],
            timezone=account['account_timezone'],
            customer_id=account_api.get('customer_id', 'no info'),
            balance=account_api.get('balance', 'no info '),
            spend=account_api.get('spend', 'no info '),
            limit=account_api.get('limit', 'no info '),
            team_name=team['team_name']
        ),
        reply_markup=kb_back_accounts
    )

