from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.constants import ADMIN
from data.repositories.accesses import AccessRepository
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.handler.admin.teams import create_team
from domain.handler.admin.teams.access import nav_access
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.teams.kb_teams import kb_teams_manage, NavigationTeams, BackTeamsManage, \
    TeamShowDetail, kb_back_teams, BackTeamManage, kb_team_detail

router = Router()

router.include_routers(
    create_team.router,
    nav_access.router
)


@router.callback_query(BackTeamsManage.filter())
async def teams_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    teams = TeamRepository().teams()

    await callback.message.edit_reply_markup(reply_markup=kb_teams_manage(teams, data.get('last_page_teams', 1)))


@router.callback_query(NavigationTeams.filter())
async def teams_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    teams = TeamRepository().teams()

    await state.update_data(last_page_team=page)

    await callback.message.edit_reply_markup(reply_markup=kb_teams_manage(teams, page))


@router.callback_query(TeamShowDetail.filter())
async def team_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    team_uuid = callback.data.split(":")[1]
    team = TeamRepository().team_by_uuid(team_uuid)
    users = len(AccessRepository().team_users_by_uuid(team_uuid))

    sum_value = 0
    # sum all value from transaction for team
    for transaction in TransactionRepository().transactions_by_team(team_uuid):
        sum_value += transaction['value']

    await state.update_data(team_uuid=team_uuid)

    await callback.message.edit_text(
        text=i18n.TEAMS.DETAIL(
            team_id=team['team_id'],
            team_name=team['team_name'],
            count_users=users,
            mcc_limit=team['mcc_limit'],
            created=team['created'],
            transactions_all=sum_value
        ),
        reply_markup=kb_team_detail
    )


@router.callback_query(BackTeamManage.filter())
async def team_detail_back(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    data = await state.get_data()
    team = TeamRepository().team_by_uuid(data['team_uuid'])
    users = len(AccessRepository().team_users_by_uuid(data['team_uuid']))

    sum_value = 0
    # sum all value from transaction for team
    for transaction in TransactionRepository().transactions_by_team(data['team_uuid']):
        sum_value += transaction['value']

    await callback.message.edit_text(
        text=i18n.TEAMS.DETAIL(
            team_id=team['team_id'],
            team_name=team['team_name'],
            count_users=users,
            mcc_limit=team['mcc_limit'],
            created=team['created'],
            transactions_all=sum_value
        ),
        reply_markup=kb_team_detail
    )
