from datetime import datetime

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext

from data.constants import CLIENT
from data.repositories.accesses import AccessRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.filters.isTeamFilter import IsTeamFilter
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.client.kb_main_client import kb_menu_client

router = Router()

router.message.middleware(UserRoleMiddleware(CLIENT))
router.callback_query.middleware(UserRoleMiddleware(CLIENT))


@router.message(Command('start'), IsAdminFilter(False), IsTeamFilter(False))
async def start_deeplink(message: Message, command: CommandObject, state: FSMContext, i18n: I18nContext):
    access_join_key = command.args
    access_by_uuid = AccessRepository().access_by_uuid(access_join_key)

    # join key is not exist
    if not access_by_uuid:
        await message.answer(i18n.JOIN_KEY.NOT_EXIST())
        return

    # join key was activated before
    if access_by_uuid['user_id']:
        await message.answer(i18n.JOIN_KEY.ACTIVATED_BEFORE())
        return

    if not AccessRepository().activate_access(access_join_key, message.from_user.id, datetime.now()):
        await message.answer(i18n.JOIN_KEY.FAIL_UPDATE())
        return

    await message.answer(i18n.JOIN_KEY.SUCCESS_UPDATE(), reply_markup=kb_menu_client)


@router.message(IsAdminFilter(False), IsTeamFilter(False))
async def all_messages_handler(message: Message, state: FSMContext, i18n: I18nContext):
    await message.answer(text=i18n.NONAME.NO_ACCESS())

