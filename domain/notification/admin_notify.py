from asyncio import gather

from aiogram import Bot
from aiogram.utils.chat_action import logger
from aiogram_i18n import I18nContext
from colorama import Style, Fore

from data.repositories.users import UserRepository


class NotificationAdmin:

    @staticmethod
    async def user_activate_bot(user_id: int, bot: Bot, i18n: I18nContext):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.NEW_USER(
                            username=user['username'],
                            user_id=str(user['user_id']),
                            join_at=user['join_at']
                        )
                    )
                    counter += 1
            except Exception as e:
                logger.error(Style.BRIGHT + f"Messaging: Failed to notify admin {admin['user_id']}: {e}")

        # Виконання надсилання повідомлень асинхронно всім адміністраторам
        await gather(*[notify_admin(admin) for admin in admins])

        logger.info(Fore.YELLOW + Style.BRIGHT + f"Messaging user_activate_bot {counter}/{len(admins)} admins successfully.")

