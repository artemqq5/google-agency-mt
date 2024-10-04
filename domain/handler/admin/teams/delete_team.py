from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.accesses import AccessRepository
from data.repositories.teams import TeamRepository
from presentation.keyboards.admin.kb_teams.kb_accesses.kb_delete_access import DeleteTeamAccessConfirmation, \
    kb_team_access_delete_confirmation, DeleteTeamAccess
from presentation.keyboards.admin.kb_teams.kb_accesses.kb_team_access import kb_back_to_team_accesses, \
    kb_back_to_team_access
from presentation.keyboards.admin.kb_teams.kb_team_delete import TeamDeleteConfirmation, kb_team_delete_confirmation
from presentation.keyboards.admin.kb_teams.kb_teams import TeamDelete, kb_back_teams, kb_back_team

router = Router()


@router.callback_query(TeamDelete.filter())
async def delete_team(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    team = TeamRepository().team_by_uuid(data['team_uuid'])
    await callback.message.edit_text(
        text=i18n.TEAMS.DELETE.WARNING(team=team['team_name']),
        reply_markup=kb_team_delete_confirmation
    )


@router.callback_query(TeamDeleteConfirmation.filter())
async def delete_team_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    if not TeamRepository().delete_team(data['team_uuid']):
        await callback.message.edit_text(
            i18n.TEAMS.DELETE.FAIL(),
            reply_markup=kb_back_team
        )
        return

    await callback.message.edit_text(i18n.TEAMS.DELETE.SUCCESS(), reply_markup=kb_back_teams)
