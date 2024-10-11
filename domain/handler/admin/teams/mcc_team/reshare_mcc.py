import uuid

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.YeezyAPI import YeezyAPI
from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.mcc_accesses import MCCAccessRepository
from data.repositories.teams import TeamRepository
from presentation.keyboards.admin.kb_teams.kb_mcc_access.kb_mcc_access import *
from presentation.keyboards.admin.kb_teams.kb_mcc_access.kb_share_mcc import NavigationMCCTeamShare, kb_mccs_team_share, \
    ShowDetailMCCTeamShare, kb_detail_share_mcc, kb_share_mcc_back, ShareMCC

router = Router()


# ReShare MCC for Team
@router.callback_query(ReShareMCC.filter())
async def reshare_mcc_team(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    team = TeamRepository().team_by_uuid(data['team_uuid'])
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    await callback.message.edit_text(i18n.TEAMS.MCC.RESHARE.CONFIRMATION(
        mcc_name=mcc['mcc_name'],
        team_name=team['team_name']
    ), reply_markup=kb_reshare_mcc_confirmation)


# ReShare MCC for Team CONFIRMATION
@router.callback_query(ReShareConfirmationMCC.filter())
async def confirmation_reshare_mcc_team(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    if not MCCAccessRepository().delete_mcc_access(data['mcc_uuid'], data['team_uuid']):
        await callback.message.edit_text(i18n.TEAMS.MCC.RESHARE.FAIL(), reply_markup=kb_detail_team_mcc_back)
        return

    await callback.message.edit_text(i18n.TEAMS.MCC.RESHARE.SUCCESS(), reply_markup=kb_team_mccs_back)
