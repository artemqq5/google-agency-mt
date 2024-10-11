from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repositories.accesses import AccessRepository
from data.repositories.mcc_accesses import MCCAccessRepository


class AccessClientMCCMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        user_id = event.from_user.id
        data2 = await data.get('state').get_data()
        if data2.get('mcc_uuid', None):
            user_access = AccessRepository().access_by_user_id(user_id)
            mcc_accesses = MCCAccessRepository().mcc_accesses_by_team_uuid(user_access['team_uuid'])
            for mcc_access in mcc_accesses:
                if data2['mcc_uuid'] == mcc_access['mcc_uuid']:
                    return await handler(event, data)

        return None


