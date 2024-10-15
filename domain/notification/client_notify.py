from asyncio import gather

from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError
from aiogram.utils.chat_action import logger
from colorama import Style, Fore

from data.repositories.accesses import AccessRepository
from data.repositories.mcc import MCCRepository
from data.repositories.users import UserRepository


class NotificationTools:

    @staticmethod
    async def push_all_clients(data: dict[str], bot: Bot, i18n):
        counter = 0
        block = 0
        other = 0

        clients = UserRepository().clients()

        async def notify_client(client):
            nonlocal counter, block, other
            try:
                if data.get('photo', None):
                    await bot.send_photo(
                        chat_id=client['user_id'],
                        photo=data['photo'],
                        caption=data['message']
                    )
                else:
                    await bot.send_message(
                        chat_id=client['user_id'],
                        text=data['message']
                    )
                counter += 1
            except TelegramForbiddenError as e:
                block += 1
                logger.error(Style.BRIGHT + f"client({client}) | push_all_clients: {e} ")
            except Exception as e:
                other += 1
                logger.error(Style.BRIGHT + f"client({client}) | push_all_clients: {e} ")

            logger.error(
                Fore.YELLOW + Style.BRIGHT + f"messaging: {counter}/{len(clients)}\nblock:{block}\nother:{other}")

        # Виконання надсилання повідомлень асинхронно всім адміністраторам
        await gather(*[notify_client(client) for client in clients])

        return i18n.MESSAGING.RESULT(send=counter, users=len(clients), block=block, other=other)

    @staticmethod
    async def push_team(data: dict[str], bot: Bot, i18n):
        counter = 0
        block = 0
        other = 0

        clients = AccessRepository().team_users_by_uuid(data['team_uuid'])
        mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

        async def notify_client(client):
            nonlocal counter, block, other
            try:
                await bot.send_message(
                    chat_id=client['user_id'],
                    text=i18n.NOTIFICATION.CLIENT.NEW_TOPUP(
                        mcc_name=mcc['mcc_name'],
                        value=data['value']
                    )
                )
                counter += 1
            except TelegramForbiddenError as e:
                block += 1
                logger.error(Style.BRIGHT + f"client({client}) | push_team: {e} ")
            except Exception as e:
                other += 1
                logger.error(Style.BRIGHT + f"client({client}) | push_team: {e} ")

            logger.error(
                Fore.YELLOW + Style.BRIGHT + f"messaging: {counter}/{len(clients)}\nblock:{block}\nother:{other}")

        # Виконання надсилання повідомлень асинхронно всім адміністраторам
        await gather(*[notify_client(client) for client in clients])

        return i18n.MESSAGING.RESULT(send=counter, users=len(clients), block=block, other=other)
