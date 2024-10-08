from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.mcc import MCCRepository
from data.repositories.teams import TeamRepository
from domain.handler.admin.teams.mcc_team import share_mcc
from presentation.keyboards.admin.kb_teams.kb_mcc_access.kb_mcc_access import *
from presentation.keyboards.admin.kb_teams.kb_teams import ManageMCCSTeam

router = Router()

router.include_routers(
    share_mcc.router
)


@router.callback_query(ManageMCCSTeam.filter())
async def manage_mcc_team(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    team = TeamRepository().team_by_uuid(data['team_uuid'])
    mccs = MCCRepository().mccs_by_team_uuid(data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.MCC.ACCESS(team_name=team['team_name']),
        reply_markup=kb_mccs_team_manage(mccs, data.get('last_page_team_mcc', 1))
    )


@router.callback_query(NavigationMCCTeam.filter())
async def mccs_teams_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()
    mccs = MCCRepository().mccs_by_team_uuid(data['team_uuid'])

    await state.update_data(last_page_team_mcc=page)

    await callback.message.edit_reply_markup(reply_markup=kb_mccs_team_manage(mccs, page))
