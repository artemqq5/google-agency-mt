from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError

from data.repositories.users import UserRepository


class NotificationTools:

    @staticmethod
    async def push_all_clients(data: dict[str], bot: Bot, i18n):
        counter = 0
        block = 0
        other = 0

        clients = UserRepository().clients()

        for client in clients:
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
                print(f"client({client}) | push_all_clients: {e} ")
            except Exception as e:
                other += 1
                print(f"client({client}) | push_all_clients: {e} ")

        print(f"messaging: {counter}/{len(clients)}\nblock:{block}\nother:{other}")
        return i18n.MESSAGING.RESULT(send=counter, users=len(clients), block=block, other=other)