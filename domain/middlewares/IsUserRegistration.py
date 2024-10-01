from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repositories.users import UserRepository
from domain.notification.admin_notify import NotificationAdmin


class UserRegistrationMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        user = event.from_user

        if not UserRepository().user(user.id):
            if not UserRepository().add(user.id, user.username, user.first_name, user.last_name, user.language_code):
                await event.bot.send_message(chat_id=user.id, text=data['i18n'].REGISTER.FAIL())
                return None

            await NotificationAdmin().user_activate_bot(user.id, data['bot'], data['i18n'])

            await event.bot.send_message(chat_id=user.id, text=data['i18n'].REGISTER.SUCCESS())

        return await handler(event, data)

