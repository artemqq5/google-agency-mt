from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.accesses import AccessRepository
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.users import UserRepository
from domain.handler.admin.teams.access import create_access, delete_access
from presentation.keyboards.admin.kb_teams.kb_accesses.kb_delete_access import kb_team_access_manage
from presentation.keyboards.admin.kb_teams.kb_team_refund import *
from presentation.keyboards.admin.kb_teams.kb_teams import kb_teams_manage, TeamRefund

router = Router()


@router.callback_query(TeamRefund.filter())
async def refund_team_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    refunded_accounts = SubAccountRepository().ref_accounts_by_team_uuid(data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.REFUND(),
        reply_markup=kb_teams_refunds(refunded_accounts, data.get('last_page_team_refund', 1))
    )


@router.callback_query(NavigationTeamRefunds.filter())
async def refunds_teams_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()
    refunded_accounts = SubAccountRepository().ref_accounts_by_team_uuid(data['team_uuid'])

    await state.update_data(last_page_team_refund=page)
    await callback.message.edit_reply_markup(reply_markup=kb_teams_refunds(refunded_accounts, page))


@router.callback_query(TeamRefundDetail.filter())
async def refund_team_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    account_uid = callback.data.split(":")[1]

    ref_account = SubAccountRepository().ref_account_by_uid(account_uid)
    mcc = MCCRepository().mcc_by_uuid(ref_account['mcc_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.REFUND.DETAIL(
            account_email=ref_account['account_email'],
            account_name=ref_account['account_name'],
            refund_value=str(ref_account['refund_value']),
            commission=str(ref_account['commission']),
            last_spend=str(ref_account['last_spend']),
            account_timezone=ref_account['account_timezone'],
            team_name=ref_account['team_name'],
            mcc_name=mcc['mcc_name'],
            status=str(ref_account['status']),
            created=str(ref_account['created']),
            completed_time=str(ref_account['completed_time'])
        ),
        reply_markup=kb_back_refund_nav
    )

