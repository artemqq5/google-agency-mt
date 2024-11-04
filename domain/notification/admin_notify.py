from asyncio import gather

from aiogram import Bot
from aiogram.utils.chat_action import logger
from aiogram_i18n import I18nContext
from colorama import Style, Fore

from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.mcc_accesses import MCCAccessRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.teams import TeamRepository
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
    async def user_create_request(user_id: int, bot: Bot, i18n: I18nContext, data):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        team = TeamRepository().team_by_uuid(data['team_uuid'])
        mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])
        balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.CREATE_TRANSACTION(
                            hash=data['hash'],
                            mcc_name=mcc['mcc_name'],
                            value=data['value'],
                            team_name=team['team_name'],
                            team_uuid=team['team_uuid'],
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

    @staticmethod
    async def user_change_email(user_id: int, bot: Bot, i18n: I18nContext, data):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        account = SubAccountRepository().account_by_uid(data['account_uid'])
        mcc = MCCRepository().mcc_by_uuid(account['mcc_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.CHANGE.EMAIL(
                            account_email=account['account_email'],
                            email=account['account_email'],
                            mcc_name=mcc['mcc_name'],
                            team_name=account['team_name'],
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
            Fore.YELLOW + Style.BRIGHT + f"Messaging user_change_email {counter}/{len(admins)} admins successfully.")

    @staticmethod
    async def user_change_email_error(user_id: int, bot: Bot, i18n: I18nContext, data):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        account = SubAccountRepository().account_by_uid(data['account_uid'])
        mcc = MCCRepository().mcc_by_uuid(account['mcc_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.CHANGE.EMAIL.ERROR(
                            account_email=account['account_email'],
                            email=account['account_email'],
                            mcc_name=mcc['mcc_name'],
                            mcc_uuid=mcc['mcc_uuid'],
                            team_name=account['team_name'],
                            team_uuid=account['team_uuid'],
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
            Fore.YELLOW + Style.BRIGHT + f"Messaging user_change_email_error {counter}/{len(admins)} admins successfully.")

    @staticmethod
    async def user_topup_account(user_id: int, bot: Bot, i18n: I18nContext, data):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        account = SubAccountRepository().account_by_uid(data['account_uid'])
        mcc = MCCRepository().mcc_by_uuid(account['mcc_uuid'])
        balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.TOPUP.ACCOUNT(
                            account_email=account['account_email'],
                            amount=data['value'],
                            mcc_name=mcc['mcc_name'],
                            balance=balance['balance'],
                            team_name=account['team_name'],
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
            Fore.YELLOW + Style.BRIGHT + f"Messaging user_topup_account {counter}/{len(admins)} admins successfully.")

    @staticmethod
    async def user_topup_account_error(user_id: int, bot: Bot, i18n: I18nContext, data, error):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        account = SubAccountRepository().account_by_uid(data['account_uid'])
        mcc = MCCRepository().mcc_by_uuid(account['mcc_uuid'])
        balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.TOPUP.ACCOUNT.ERROR(
                            account_email=account['account_email'],
                            error=error,
                            amount=data['value'],
                            mcc_name=mcc['mcc_name'],
                            mcc_uuid=mcc['mcc_uuid'],
                            balance=balance['balance'],
                            balance_uuid=balance['balance_uuid'],
                            team_name=account['team_name'],
                            team_uuid=account['team_uuid'],
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
            Fore.YELLOW + Style.BRIGHT + f"Messaging user_topup_account_error {counter}/{len(admins)} admins successfully.")

    @staticmethod
    async def user_refund_account(user_id: int, bot: Bot, i18n: I18nContext, data, account):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])
        balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.REFUND.ACCOUNT(
                            account_email=account['account_email'],
                            balance=balance['balance'],
                            mcc_name=mcc['mcc_name'],
                            team_name=account['team_name'],
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
            Fore.YELLOW + Style.BRIGHT + f"Messaging user_refund_account {counter}/{len(admins)} admins successfully.")

    @staticmethod
    async def user_refund_account_error(user_id: int, bot: Bot, i18n: I18nContext, data, account, error):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])
        balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.REFUND.ACCOUNT.ERROR(
                            error=error,
                            account_email=account['account_email'],
                            balance=balance['balance'],
                            mcc_name=mcc['mcc_name'],
                            mcc_uuid=mcc['mcc_uuid'],
                            balance_uuid=balance['balance_uuid'],
                            team_name=account['team_name'],
                            team_uuid=account['team_uuid'],
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
            Fore.YELLOW + Style.BRIGHT + f"Messaging user_refund_account_error {counter}/{len(admins)} admins successfully.")

    @staticmethod
    async def user_create_account(user_id: int, bot: Bot, i18n: I18nContext, data, account_uid):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        account = SubAccountRepository().account_by_uid(account_uid)
        mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])
        mcc_access = MCCAccessRepository().mcc_access(data['mcc_uuid'], data['team_uuid'])
        balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.CREATE.ACCOUNT(
                            account_email=account['account_email'],
                            amount=data['amount'],
                            mcc_name=mcc['mcc_name'],
                            team_name=mcc_access['team_name'],
                            limit=mcc_access['account_available'],
                            balance=balance['balance'],
                            email=account['account_email'],
                            timezone=account['account_timezone'],
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
            Fore.YELLOW + Style.BRIGHT + f"Messaging user_create_account {counter}/{len(admins)} admins successfully.")

    @staticmethod
    async def user_create_account_error(user_id: int, bot: Bot, i18n: I18nContext, data, error):
        counter = 0

        # Створення екземпляра UserRepository
        admins = UserRepository().admins()
        user = UserRepository().user(user_id)
        mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])
        mcc_access = MCCAccessRepository().mcc_access(data['mcc_uuid'], data['team_uuid'])
        balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])

        # Функція для надсилання повідомлень адміністраторам
        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.CREATE.ACCOUNT.ERROR(
                            account_email=data['email'],
                            amount=data['amount'],
                            error=error,
                            mcc_name=mcc['mcc_name'],
                            mcc_uuid=mcc['mcc_uuid'],
                            team_name=mcc_access['team_name'],
                            team_uuid=mcc_access['team_uuid'],
                            email=data['email'],
                            limit=mcc_access['account_available'],
                            balance=balance['balance'],
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
            Fore.YELLOW + Style.BRIGHT + f"Messaging user_create_account_error {counter}/{len(admins)} admins successfully.")

