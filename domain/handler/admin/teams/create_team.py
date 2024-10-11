import uuid

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.mcc_accesses import MCCAccessRepository
from data.repositories.teams import TeamRepository
from domain.states.admin.team.CreateTeamState import CreateTeamState
from presentation.keyboards.admin.kb_teams.kb_teams import CreateNewTeam, kb_back_teams

router = Router()


@router.callback_query(CreateNewTeam.filter())
async def create_team_start(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(CreateTeamState.TeamName)
    await callback.message.edit_text(text=i18n.TEAMS.CREATE.NAME(), reply_markup=kb_back_teams)


@router.message(CreateTeamState.TeamName)
async def save_team_name(message: Message, state: FSMContext, i18n: I18nContext):
    team_name = message.text
    if len(team_name) >= 50:
        await message.answer(
            text=i18n.TEAMS.CREATE.NAME_ERROR(symballs=len(team_name)),
            reply_markup=kb_back_teams
        )
        return

    await state.set_state(None)

    # generate UUID for team
    team_uuid = uuid.uuid4()

    # create team in database
    if not TeamRepository().create_team(team_name, team_uuid):
        await message.answer(i18n.TEAMS.CREATE.FAIL(error="Create Team DB"), reply_markup=kb_back_teams)
        return

    # get all general MCC for all teams
    generals_mcc = MCCRepository().generals_mcc()

    # create balance for every general mcc
    for mcc in generals_mcc:
        # generate UUID for balance
        balance_uuid = uuid.uuid4()

        # generate UUID for mcc access
        mcc_access_team = uuid.uuid4()

        if not MCCAccessRepository().share_mcc(mcc_access_team, mcc['mcc_uuid'], team_uuid, team_name):
            await message.edit_text(i18n.TEAMS.CREATE.FAIL(error=f"Can`t Create access for MCC"),
                                    reply_markup=kb_back_teams)
            return

        if not BalanceRepository().create(balance_uuid, mcc['mcc_uuid'], team_uuid, team_name):
            await message.answer(text=i18n.TEAMS.CREATE.FAIL(error=f"Can`t Create balance for MCC"),
                                 reply_markup=kb_back_teams)
            return

    await message.answer(text=i18n.TEAMS.CREATE.SUCCESS(team=team_name), reply_markup=kb_back_teams)

