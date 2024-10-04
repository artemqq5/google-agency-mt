import uuid
from uuid import UUID

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.constants import ADMIN
from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.teams import TeamRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.middlewares.IsUserRole import UserRoleMiddleware
from domain.states.admin.team.CreateTeamState import CreateTeamState
from domain.states.admin.team.TeamMCCLimitState import TeamMCCLimitState
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_teams.kb_teams import kb_teams_manage, CreateNewTeam, kb_back_teams, TeamMCCLimit, \
    kb_back_team

router = Router()


@router.callback_query(TeamMCCLimit.filter())
async def edit_team_mcc_limit(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    team = TeamRepository().team_by_uuid(data['team_uuid'])

    await state.set_state(TeamMCCLimitState.Limit)

    await callback.message.edit_text(
        text=i18n.TEAMS.MCC.LIMIT.VALUE(team=team['team_name']),
        reply_markup=kb_back_team
    )


@router.message(TeamMCCLimitState.Limit)
async def save_team_name(message: Message, state: FSMContext, i18n: I18nContext):
    try:
        mcc_limit = int(message.text)
        if mcc_limit < 0 or mcc_limit > 999:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.TEAMS.MCC.LIMIT.VALUE_ERROR(), reply_markup=kb_back_team)
        return

    data = await state.get_data()

    if TeamRepository().team_by_uuid(data['team_uuid'])['mcc_limit'] == mcc_limit:
        await message.answer(i18n.TEAMS.MCC.LIMIT.VALUE_DUBL(limit=mcc_limit), reply_markup=kb_back_team)
        return

    await state.set_state(None)

    if not TeamRepository().update_team_mcc_limit(data['team_uuid'], mcc_limit):
        await message.answer(i18n.TEAMS.MCC.LIMIT.FAIL(), reply_markup=kb_back_team)
        return

    await message.answer(i18n.TEAMS.MCC.LIMIT.SUCCESS(limit=mcc_limit), reply_markup=kb_back_team)

