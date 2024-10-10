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


@router.callback_query(ShareMCCTeam.filter())
async def share_mcc_team_list(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    team = TeamRepository().team_by_uuid(data['team_uuid'])
    mccs = MCCRepository().available_mccs_by_team_uuid(data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.MCC.SHARE.CHOICE(team_name=team['team_name']),
        reply_markup=kb_mccs_team_share(mccs, data.get('last_page_team_mcc_share', 1))
    )


@router.callback_query(NavigationMCCTeamShare.filter())
async def share_mccs_teams_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()
    mccs = MCCRepository().available_mccs_by_team_uuid(data['team_uuid'])

    await state.update_data(last_page_team_mcc_share=page)

    await callback.message.edit_reply_markup(reply_markup=kb_mccs_team_share(mccs, page))


@router.callback_query(ShowDetailMCCTeamShare.filter())
async def share_mcc_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
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
        reply_markup=kb_detail_share_mcc
    )


# Share MCC for Team
@router.callback_query(ShareMCC.filter())
async def share_mcc_team(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    team = TeamRepository().team_by_uuid(data['team_uuid'])
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    # generate UUID for mcc access
    mcc_access_team = uuid.uuid4()

    if not MCCAccessRepository().share_mcc(mcc_access_team, data['mcc_uuid'], data['team_uuid'], team['team_name']):
        await callback.message.edit_text(i18n.TEAMS.MCC.SHARE.FAIL(error="Access DB"), reply_markup=kb_share_mcc_back)
        return

    # if balance not exist, create new balance for mcc
    if not BalanceRepository().balance(mcc['mcc_uuid'], data['team_uuid']):
        # generate UUID for balance
        balance_uuid = uuid.uuid4()
        if not BalanceRepository().create(balance_uuid, mcc['mcc_uuid'], data['team_uuid'], team['team_name']):
            await callback.message.answer(text=i18n.TEAMS.MCC.SHARE.FAIL(error="Balance"), reply_markup=kb_share_mcc_back)
            return

    await callback.message.edit_text(i18n.TEAMS.MCC.SHARE.SUCCESS(
        mcc_name=mcc['mcc_name'],
        team_name=team['team_name']
    ), reply_markup=kb_share_mcc_back)
