from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext, L

from data.constants import ADMIN
from data.repositories.mcc import MCCRepository
from data.repositories.teams import TeamRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.handler.admin.mcc import nav_mcc
from domain.handler.admin.teams import nav_teams
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_mcc.kb_mcc import kb_mccs_manage
from presentation.keyboards.admin.kb_teams.kb_teams import kb_teams_manage

router = Router()

router.include_routers(
    nav_teams.router,
    nav_mcc.router
)

router.message.middleware(UserRoleMiddleware(ADMIN))
router.callback_query.middleware(UserRoleMiddleware(ADMIN))


@router.message(Command("start"), IsAdminFilter(True))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.MENU(), reply_markup=kb_menu_admin)


@router.message(F.text == L.ADMIN.TEAMS())
async def teams_manage(message: Message, i18n: I18nContext):
    teams = TeamRepository().teams()
    await message.answer(i18n.ADMIN.TEAMS(), reply_markup=kb_teams_manage(teams))


@router.message(F.text == L.ADMIN.MCC())
async def mcc_manage(message: Message, i18n: I18nContext, state: FSMContext):
    mccs = MCCRepository().mccs()
    await message.answer(i18n.ADMIN.MCC(), reply_markup=kb_mccs_manage(mccs))
