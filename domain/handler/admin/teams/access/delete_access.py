from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.accesses import AccessRepository
from presentation.keyboards.admin.kb_teams.kb_accesses.kb_delete_access import DeleteTeamAccessConfirmation, \
    kb_team_access_delete_confirmation, DeleteTeamAccess
from presentation.keyboards.admin.kb_teams.kb_accesses.kb_team_access import kb_back_to_team_accesses, \
    kb_back_to_team_access

router = Router()


@router.callback_query(DeleteTeamAccess.filter())
async def delete_team_access(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.edit_text(
        text=i18n.TEAMS.ACCESS.DELETE.WARNING(),
        reply_markup=kb_team_access_delete_confirmation
    )


@router.callback_query(DeleteTeamAccessConfirmation.filter())
async def delete_team_access_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    if not AccessRepository().delete_access_by_uuid(data['access_uuid']):
        await callback.message.edit_text(
            i18n.TEAMS.ACCESS.DELETE.FAIL(),
            reply_markup=kb_back_to_team_access(data['access_uuid'])
        )
        return

    await callback.message.edit_text(i18n.TEAMS.ACCESS.DELETE.SUCCESS(), reply_markup=kb_back_to_team_accesses)
