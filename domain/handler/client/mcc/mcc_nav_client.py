from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.YeezyAPI import YeezyAPI
from data.constants import ADMIN
from data.repositories.accesses import AccessRepository
from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.mcc_accesses import MCCAccessRepository
from data.repositories.sub_accounts_mcc import SubAccountMCC
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.handler.admin.mcc import add_new_mcc
from domain.handler.admin.mcc.accounts import nav_accounts
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.handler.client.mcc.accounts import accounts_nav_client
from domain.middlewares.AccessClientMCC import AccessClientMCCMiddleware
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_mcc.kb_accounts import kb_accounts_manage
from presentation.keyboards.client.kb_mcc.kb_accounts import kb_accounts_manage_client, ShowDetailClientMCCBack
from presentation.keyboards.client.kb_mcc.kb_mcc import kb_client_mccs_manage, NavigationClientMCC, \
    BackMCCSManageClient, ShowDetailClientMCC

router = Router()

router.include_routers(
    accounts_nav_client.router
)


@router.callback_query(BackMCCSManageClient.filter())
async def mccs_client_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    # get available mcc for team by team_uuid
    mccs = MCCRepository().mccs_by_team_uuid(data['team_uuid'])
    await callback.message.edit_text(text=i18n.CLIENT.MCC(), reply_markup=kb_client_mccs_manage(mccs, data.get('last_page_mccs', 1)))


@router.callback_query(NavigationClientMCC.filter())
async def mccs_client_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    page = int(callback.data.split(":")[1])
    mccs = MCCRepository().mccs_by_team_uuid(data['team_uuid'])

    await state.update_data(last_page_mcc=page)
    await callback.message.edit_reply_markup(reply_markup=kb_client_mccs_manage(mccs, page))


@router.callback_query(ShowDetailClientMCC.filter())
async def mcc_client_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    mcc_uuid = callback.data.split(":")[1]
    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(mcc_uuid)
    mcc_balance = BalanceRepository().balance(mcc_uuid, data['team_uuid'])
    mcc_access = MCCAccessRepository().mcc_access(mcc_uuid, data['team_uuid'])

    await state.update_data(mcc_uuid=mcc_uuid)

    # Get Accounts From DataBase
    accounts = SubAccountMCC().accounts_by_team_uuid(mcc_uuid, data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.CLIENT.MCC.DETAIL(
            name=mcc['mcc_name'],
            account_available=mcc_access['account_available'],
            balance=mcc_balance['balance'],
        ),
        reply_markup=kb_accounts_manage_client(accounts, 1)
    )


@router.callback_query(ShowDetailClientMCCBack.filter())
async def mcc_client_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])
    mcc_balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])
    mcc_access = MCCAccessRepository().mcc_access(data['mcc_uuid'], data['team_uuid'])

    # Get Accounts From DataBase
    accounts = SubAccountMCC().accounts_by_team_uuid(data['mcc_uuid'], data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.CLIENT.MCC.DETAIL(
            name=mcc['mcc_name'],
            account_available=mcc_access['account_available'],
            balance=mcc_balance['balance'],
        ),
        reply_markup=kb_accounts_manage_client(accounts, data.get('last_page_accounts', 1))
    )
