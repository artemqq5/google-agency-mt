from aiogram import Router, F, Bot
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
from domain.handler.admin.mcc import add_new_mcc
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.middlewares.IsUserRole import UserRoleMiddleware
from domain.states.admin.account.ChangeTeamAccountState import ChangeTeamAccountState
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_mcc.kb_accounts import *

router = Router()


@router.callback_query(ChangeTeamAccount.filter())
async def change_team_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ChangeTeamAccountState.TeamUUID)
    await callback.message.edit_text(i18n.ADMIN.ACCOUNT.CHANGE_TEAM.UUID(), reply_markup=kb_back_account)


@router.message(ChangeTeamAccountState.TeamUUID)
async def create_team_uuid_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()
    new_team_uuid = message.text

    # account already has that team
    account = SubAccountRepository().account_by_uid(data['account_uid'])
    if account['team_uuid'] == new_team_uuid:
        await message.answer(i18n.ADMIN.ACCOUNT.CHANGE_TEAM.EXIST(), reply_markup=kb_back_account)
        return

    # check if team exist
    team = TeamRepository().team_by_uuid(new_team_uuid)
    if not team:
        await message.answer(i18n.ADMIN.ACCOUNT.CHANGE_TEAM.ERROR(), reply_markup=kb_back_account)
        return

    # try update subaccount
    if not SubAccountRepository().update_team(team['team_uuid'], team['team_name'], data['account_uid']):
        await message.answer(i18n.ADMIN.ACCOUNT.CHANGE_TEAM.FAIL(), reply_markup=kb_back_account)
        return

    await message.answer(i18n.ADMIN.ACCOUNT.CHANGE_TEAM.SUCCESS(team_name=team['team_name']), reply_markup=kb_back_account)
