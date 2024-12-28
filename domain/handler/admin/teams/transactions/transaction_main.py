from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.constants import ADMIN
from data.repositories.accesses import AccessRepository
from data.repositories.sub_transactions import SubTransactionRepository
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.handler.admin.teams.mcc_team import manage_team_mcc
from domain.handler.admin.teams.transactions import transaction_mcc, transaction_account, transaction_tax
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_teams.kb_team_transaction import kb_teams_transaction_mcc
from presentation.keyboards.admin.kb_teams.kb_teams import kb_teams_manage, NavigationTeams, BackTeamsManage, \
    TeamShowDetail, kb_back_teams, BackTeamManage, kb_back_to_team, TeamTransaction, kb_transaction_choice_team, \
    TeamTransactionMCC, TeamTransactionAccount

router = Router()

router.include_routers(
    transaction_mcc.router,
    transaction_account.router,
    transaction_tax.router
)


@router.callback_query(TeamTransaction.filter())
async def team_transaction_choice(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.edit_text(text=i18n.TEAMS.TRANSACTIONS(), reply_markup=kb_transaction_choice_team)


