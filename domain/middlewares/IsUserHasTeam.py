from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repositories.accesses import AccessRepository
from data.repositories.teams import TeamRepository


class UserHasTeamMiddleware(BaseMiddleware):

    def __init__(self, has_team: bool = True):
        self.has_team = has_team

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        if self.has_team:
            access = AccessRepository().access_by_user_id(event.from_user.id)
            if not access or not TeamRepository().team_by_uuid(access['team_uuid']):
                return
        else:
            access = AccessRepository().access_by_user_id(event.from_user.id)
            if access and TeamRepository().team_by_uuid(access['team_uuid']):
                return

        return await handler(event, data)
