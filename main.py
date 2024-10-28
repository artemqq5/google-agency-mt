import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore
from colorama import init

import private_config
from domain.handler.admin import dp_admin
from domain.handler.all import dp_all
from domain.handler.client import dp_client

from domain.handler.noname import dp_noname
from domain.middlewares.IsUserRegistration import UserRegistrationMiddleware
from domain.middlewares.LocaleManager import LocaleManager

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(
    dp_all.router,
    dp_admin.router,
    dp_client.router,
    dp_noname.router,
)


async def main():

    # logs
    init(autoreset=True)
    logging.basicConfig(level=logging.INFO)

    # bot settings
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=private_config.BOT_TOKEN, default=default_properties, timeout=60)

    try:
        # localization middleware
        i18n_middleware = I18nMiddleware(
            core=FluentRuntimeCore(path='presentation/locales'),
            default_locale='en',
            manager=LocaleManager()
        )

        i18n_middleware.setup(dp)

        dp.message.outer_middleware(UserRegistrationMiddleware())  # register if user not registered
        dp.callback_query.outer_middleware(UserRegistrationMiddleware())  # register if user not registered

        # start bot
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        print(f"start bot: {e}")
        return


if __name__ == '__main__':
    asyncio.run(main())

