from asyncio import gather

from aiogram import Bot
from aiogram.utils.chat_action import logger
from aiogram_i18n import I18nContext
from colorama import Style, Fore

from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.transactions import TransactionRepository
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
                            username=str(user['username']),
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

    @staticmethod
    async def user_create_transaction(user_id: int, bot: Bot, i18n: I18nContext, transaction_uuid):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        transaction = TransactionRepository().transaction(transaction_uuid)
        mcc = MCCRepository().mcc_by_uuid(transaction['mcc_uuid'])
        balance = BalanceRepository().balance(transaction['mcc_uuid'], transaction['team_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.CREATE_TRANSACTION(
                            id_transaction=transaction['id'],
                            uuid_transaction=transaction['transaction_uuid'],
                            mcc_name=mcc['mcc_name'],
                            value=transaction['value'],
                            team_name=transaction['team_name'],
                            team_uuid=transaction['team_uuid'],
                            balance_team_value=balance['balance'],
                            username=str(user['username']),
                            user_id=str(user['user_id']),
                        )
                    )
                    counter += 1
            except Exception as e:
                logger.error(Style.BRIGHT + f"Messaging: Failed to notify admin {admin['user_id']}: {e}")

        # Виконання надсилання повідомлень асинхронно всім адміністраторам
        await gather(*[notify_admin(admin) for admin in admins])

        logger.info(
            Fore.YELLOW + Style.BRIGHT + f"Messaging user_create_transaction {counter}/{len(admins)} admins successfully.")

