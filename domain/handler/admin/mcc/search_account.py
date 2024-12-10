

import uuid

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
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.middlewares.IsUserRole import UserRoleMiddleware
from domain.states.admin.account.SearchAccountState import SearchAccountState
from domain.states.admin.mcc.AddNewMCCState import AddNewMCCState
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_mcc.kb_accounts import kb_back_accounts, kb_back_search
from presentation.keyboards.admin.kb_mcc.kb_mcc import *

router = Router()


@router.callback_query(SearchAccount.filter())
async def account_search(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(SearchAccountState.email)
    await callback.message.answer(i18n.ADMIN.SEARCH.ACCOUNT.EMAIL())


@router.message(SearchAccountState.email)
async def email_account_search(message: Message, state: FSMContext, i18n: I18nContext):
    account = SubAccountRepository().account_by_email(message.text)

    if not account:
        await message.answer(i18n.ADMIN.SEARCH.ACCOUNT.NOTHING())
        await message.answer(i18n.ADMIN.SEARCH.ACCOUNT.EMAIL())
        return

    mcc = MCCRepository().mcc_by_uuid(account['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await message.answer(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    # Get Account API info
    account_api_response = YeezyAPI().get_verify_account(auth['token'], account['account_uid'])
    if not account_api_response:
        await message.answer(i18n.ADMIN.ACCOUNT.NO_VERIFY_YET(), show_alert=True)
        return

    account_api = account_api_response.get('accounts', [{}])[0]

    await state.update_data(account_uid=account['account_uid'])
    await state.update_data(mcc_uuid=account['mcc_uuid'])

    await message.answer(
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
            team_name=account['team_name']
        ),
        reply_markup=kb_back_search
    )

