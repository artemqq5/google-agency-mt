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
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_teams.kb_teams import kb_teams_manage, CreateNewTeam, kb_back_teams

router = Router()


@router.callback_query(CreateNewTeam.filter())
async def create_team(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(CreateTeamState.TeamName)
    await callback.message.edit_text(text=i18n.TEAMS.CREATE.NAME(), reply_markup=kb_back_teams)


@router.message(CreateTeamState.TeamName)
async def save_team_name(message: Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) >= 50:
        await message.answer(
            text=i18n.TEAMS.CREATE.NAME_ERROR(symballs=len(message.text)),
            reply_markup=kb_back_teams
        )
        return

    await state.update_data(team_name=message.text)
    await state.set_state(CreateTeamState.MCCLimit)
    await message.answer(text=i18n.TEAMS.CREATE.LIMIT(), reply_markup=kb_back_teams)


@router.message(CreateTeamState.MCCLimit)
async def save_team_limit(message: Message, state: FSMContext, i18n: I18nContext):
    try:
        mcc_limit = int(message.text)
        if mcc_limit < 0 or mcc_limit > 999:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.TEAMS.CREATE.LIMIT_ERROR(), reply_markup=kb_back_teams)
        return

    data = await state.get_data()
    await state.set_state(None)

    # generate UUID for team
    team_uuid = uuid.uuid4()

    # create team in database
    if not TeamRepository().create_team(data['team_name'], team_uuid, mcc_limit):
        await message.answer(i18n.TEAMS.CREATE.FAIL(error="Create Team DB"), reply_markup=kb_back_teams)
        return

    # get all general MCC for all teams
    generals_mcc = MCCRepository().generals_mcc()

    # create balance for every general mcc
    for mcc in generals_mcc:
        # generate UUID for balance
        balance_uuid = uuid.uuid4()
        if not BalanceRepository().create(balance_uuid, mcc['mcc_uuid'], team_uuid):
            await message.answer(text=i18n.TEAMS.CREATE.FAIL(error=f"Cant Create balance for MCC"), reply_markup=kb_back_teams)
            return

    await message.answer(text=i18n.TEAMS.CREATE.SUCCESS(team=data['team_name']), reply_markup=kb_back_teams)
