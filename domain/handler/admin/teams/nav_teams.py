from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.accesses import AccessRepository
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.handler.admin.teams.mcc_team import manage_team_mcc
from domain.handler.admin.teams.refund import refund_history
from domain.handler.admin.teams.transactions import transaction_main
from presentation.keyboards.admin.kb_teams.kb_teams import kb_teams_manage, NavigationTeams, BackTeamsManage, \
    TeamShowDetail, BackTeamManage, kb_back_to_team

router = Router()

router.include_routers(
    create_team.router,
    delete_team.router,
    nav_access.router,
    manage_team_mcc.router,
    transaction_main.router,
    refund_history.router
)


@router.callback_query(BackTeamsManage.filter())
async def teams_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    teams = TeamRepository().teams()

    await callback.message.edit_text(text=i18n.ADMIN.TEAMS(),
                                     reply_markup=kb_teams_manage(teams, data.get('last_page_teams', 1)))


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
            team_uuid=team['team_uuid'],
            count_users=users,
            created=team['created'],
            transactions_all=sum_value
        ),
        reply_markup=kb_back_to_team
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
            team_uuid=team['team_uuid'],
            count_users=users,
            created=team['created'],
            transactions_all=sum_value
        ),
        reply_markup=kb_back_to_team
    )
