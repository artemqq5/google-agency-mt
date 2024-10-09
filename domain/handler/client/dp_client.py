from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext, L

from data.constants import CLIENT
from domain.filters.isAdminFilter import IsAdminFilter
from domain.filters.isTeamFilter import IsTeamFilter
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.client.kb_main_client import kb_menu_client

router = Router()

router.message.middleware(UserRoleMiddleware(CLIENT))
router.callback_query.middleware(UserRoleMiddleware(CLIENT))


@router.message(Command("start"), IsAdminFilter(False), IsTeamFilter(True))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.MENU(), reply_markup=kb_menu_client)


@router.message(F.text == L.CLIENT.ACCOUNTS(), IsTeamFilter(True))
async def accounts_manage(message: Message, i18n: I18nContext, state: FSMContext):
    await message.answer("Waiting for develop...")

