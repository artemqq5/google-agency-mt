from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repositories.mcc_accesses import MCCAccessRepository
from presentation.keyboards.client.kb_mcc.kb_accounts import kb_back_detail_mcc


class MCCLimitClientMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        data2 = await data.get('state').get_data()

        if data2.get('mcc_uuid', None) and data2.get('team_uuid', None):
            mcc_access = MCCAccessRepository().mcc_access(data2['mcc_uuid'], data2['team_uuid'])
            if mcc_access['account_available'] > 0:
                return await handler(event, data)

            if isinstance(event, types.Message):
                await event.answer(data['i18n'].CLIENT.ACCOUNT.CREATE.LIMIT(), reply_markup=kb_back_detail_mcc)

            elif isinstance(event, types.CallbackQuery):
                await event.answer(data['i18n'].CLIENT.ACCOUNT.CREATE.LIMIT(), show_alert=True)

        return None
