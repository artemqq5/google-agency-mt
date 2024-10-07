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
from domain.handler.admin.mcc import add_new_mcc
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.handler.admin.teams.mcc_limit import mcc_limit_team
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_mcc.kb_mcc import *

router = Router()

router.include_routers(
    add_new_mcc.router,
)


@router.callback_query(BackMCCSManage.filter())
async def mccs_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    mccs = MCCRepository().mccs()

    await callback.message.edit_text(text=i18n.ADMIN.MCC(), reply_markup=kb_mccs_manage(mccs, data.get('last_page_mccs', 1)))


@router.callback_query(NavigationMCC.filter())
async def mccs_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    mccs = MCCRepository().mccs()

    await state.update_data(last_page_mcc=page)

    await callback.message.edit_reply_markup(reply_markup=kb_mccs_manage(mccs, page))


# @router.callback_query(TeamShowDetail.filter())
# async def team_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
#     team_uuid = callback.data.split(":")[1]
#     team = TeamRepository().team_by_uuid(team_uuid)
#     users = len(AccessRepository().team_users_by_uuid(team_uuid))
#
#     sum_value = 0
#     # sum all value from transaction for team
#     for transaction in TransactionRepository().transactions_by_team(team_uuid):
#         sum_value += transaction['value']
#
#     await state.update_data(team_uuid=team_uuid)
#
#     await callback.message.edit_text(
#         text=i18n.TEAMS.DETAIL(
#             team_id=team['team_id'],
#             team_name=team['team_name'],
#             count_users=users,
#             mcc_limit=team['mcc_limit'],
#             created=team['created'],
#             transactions_all=sum_value
#         ),
#         reply_markup=kb_back_to_team
#     )
#
#
# @router.callback_query(BackTeamManage.filter())
# async def team_detail_back(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
#     data = await state.get_data()
#     team = TeamRepository().team_by_uuid(data['team_uuid'])
#     users = len(AccessRepository().team_users_by_uuid(data['team_uuid']))
#
#     sum_value = 0
#     # sum all value from transaction for team
#     for transaction in TransactionRepository().transactions_by_team(data['team_uuid']):
#         sum_value += transaction['value']
#
#     await callback.message.edit_text(
#         text=i18n.TEAMS.DETAIL(
#             team_id=team['team_id'],
#             team_name=team['team_name'],
#             count_users=users,
#             mcc_limit=team['mcc_limit'],
#             created=team['created'],
#             transactions_all=sum_value
#         ),
#         reply_markup=kb_back_to_team
#     )
