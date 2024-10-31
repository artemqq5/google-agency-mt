from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.YeezyAPI import YeezyAPI
from data.constants import ADMIN
from data.repositories.accesses import AccessRepository
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.handler.admin.mcc import add_new_mcc, mcc_is_general, create_new_account
from domain.handler.admin.mcc.accounts import nav_accounts
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_mcc.kb_accounts import kb_accounts_manage
from presentation.keyboards.admin.kb_mcc.kb_mcc import *

router = Router()

router.include_routers(
    add_new_mcc.router,
    nav_accounts.router,
    mcc_is_general.router,
    create_new_account.router
)


@router.callback_query(BackMCCSManage.filter())
async def mccs_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    mccs = MCCRepository().mccs()

    await callback.message.edit_text(text=i18n.ADMIN.MCC(), reply_markup=kb_mccs_manage(mccs, data.get('last_page_mccs', 1)))


@router.callback_query(NavigationMCC.filter())
async def mccs_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    mccs = MCCRepository().mccs()

    await state.update_data(last_page_mcc=page)

    await callback.message.edit_reply_markup(reply_markup=kb_mccs_manage(mccs, page))


@router.callback_query(ShowDetailMCC.filter())
async def mcc_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    mcc_uuid = callback.data.split(":")[1]
    mcc = MCCRepository().mcc_by_uuid(mcc_uuid)

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.answer(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    # Get master balance with Auth Token MCC
    mcc_balance = YeezyAPI().get_master_balance(auth['token'])

    # Get Accounts From DataBase
    accounts = SubAccountRepository().accounts_by_mcc_uuid(mcc_uuid)
    print(mcc_uuid)
    print(accounts)
    await state.update_data(mcc_uuid=mcc_uuid)

    status = '✅' if bool(mcc['is_general']) else '❌'

    await callback.message.edit_text(
        text=i18n.MCC.DETAIL(
            name=mcc['mcc_name'],
            balance=mcc_balance.get('balances', {}).get('USD', 'Error. No USD balance '),
            general=status
        ),
        reply_markup=kb_accounts_manage(accounts, mcc_uuid, 1)
    )
