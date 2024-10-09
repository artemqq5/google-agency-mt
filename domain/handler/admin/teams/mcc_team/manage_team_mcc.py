from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.YeezyAPI import YeezyAPI
from data.repositories.mcc import MCCRepository
from data.repositories.mcc_accesses import MCCAccessRepository
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


@router.callback_query(ShowDetailMCCTeam.filter())
async def team_mcc_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    mcc_uuid = callback.data.split(":")[1]
    mcc = MCCRepository().mcc_by_uuid(mcc_uuid)

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.answer(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    # Get master balance with Auth Token MCC
    mcc_balance = YeezyAPI().get_master_balance(auth['token'])

    await state.update_data(mcc_uuid=mcc_uuid)

    await callback.message.edit_text(
        text=i18n.MCC.DETAIL(
            name=mcc['mcc_name'],
            balance=mcc_balance.get('balances', {}).get('USD', 'Error. No USD balance '),
        ),
        reply_markup=kb_detail_team_mcc
    )


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

    await callback.message.edit_text(i18n.TEAMS.MCC.RESHARE.SUCCESS(), reply_markup=kb_detail_team_mcc_back)
