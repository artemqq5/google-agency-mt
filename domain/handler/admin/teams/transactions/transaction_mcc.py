from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.constants import ADMIN
from data.repositories.accesses import AccessRepository
from data.repositories.mcc import MCCRepository
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.handler.admin.teams.mcc_team import manage_team_mcc
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_teams.kb_team_transaction import kb_teams_transaction_mcc, \
    NavigationeamTransactionMCC, TeamTransactionMCCDetail, kb_transaction_mcc_back
from presentation.keyboards.admin.kb_teams.kb_teams import kb_teams_manage, NavigationTeams, BackTeamsManage, \
    TeamShowDetail, kb_back_teams, BackTeamManage, kb_back_to_team, TeamTransaction, kb_transaction_choice_team, \
    TeamTransactionMCC

router = Router()


@router.callback_query(TeamTransactionMCC.filter())
async def team_transactions_mcc(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    transactions_mcc = TransactionRepository().transactions_by_team(data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.TRANSACTIONS.MCC(),
        reply_markup=kb_teams_transaction_mcc(transactions_mcc, data.get('last_page_transaction_mcc', 1))
    )


@router.callback_query(NavigationeamTransactionMCC.filter())
async def transactions_mcc_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()
    transactions_mcc = TransactionRepository().transactions_by_team(data['team_uuid'])

    await state.update_data(last_page_transaction_mcc=page)

    await callback.message.edit_reply_markup(reply_markup=kb_teams_transaction_mcc(transactions_mcc, page))


@router.callback_query(TeamTransactionMCCDetail.filter())
async def transaction_mcc_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    transaction_uuid = callback.data.split(":")[1]
    transaction = TransactionRepository().transaction(transaction_uuid)
    mcc = MCCRepository().mcc_by_uuid(transaction['mcc_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.TRANSACTIONS.MCC.DETAIL(
            id_transaction=transaction['id'],
            uuid_transaction=transaction['transaction_uuid'],
            mcc_name=mcc['mcc_name'],
            value=transaction['value'],
            date=str(transaction['created'])
        ),
        reply_markup=kb_transaction_mcc_back
    )
