import asyncio
import logging
from collections import defaultdict

from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError

from data.repositories.accesses import AccessRepository
from domain.tools.send_large_message import send_large_message

# Налаштовуємо логування
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


async def send_taxes_info_to_teams(transactions: list[dict], bot: Bot, message, i18n):
    # Сортуємо транзакції за team_uuid
    grouped_transactions = defaultdict(list)
    for transaction in transactions:
        grouped_transactions[transaction['team_uuid']].append(transaction)

    result_message = []

    # Проходимо по кожній команді
    for team_uuid, team_transactions in grouped_transactions.items():
        # Рахуємо загальну суму та кількість комісій
        total_amount = sum(t['amount'] for t in team_transactions)
        total_commissions = len(team_transactions)

        # Логуємо інформацію про команду
        logger.info(
            f"Processing team_uuid: {team_uuid}, Total Amount: {total_amount}, Total Commissions: {total_commissions}")

        # Створюємо текст повідомлення
        message_text = i18n.NOTIFICATION.TEAM.COMMISSIONS_REPORT(
            taxes_count=str(total_commissions),
            taxes_amount=str(total_amount),
        )

        # Отримуємо учасників команди
        clients = AccessRepository().team_users_by_uuid(team_uuid)
        logger.info(f"Found {len(clients)} clients for team_uuid: {team_uuid}")

        # Відправляємо повідомлення всім учасникам команди
        result = await notify_team_members(clients, message_text, bot, i18n, team_transactions[0]['team_name'])
        result_message.append(result)

    await send_large_message(message, "\n\n".join(result_message))


async def notify_team_members(clients: list[dict], message_text: str, bot: Bot, i18n, team_name):
    counter = 0
    block = 0
    other = 0

    async def notify_client(client):
        nonlocal counter, block, other
        try:
            await bot.send_message(
                chat_id=client['user_id'],
                text=message_text
            )
            counter += 1
        except TelegramForbiddenError as _:
            block += 1
            logger.warning(f"User blocked bot: user_id={client['user_id']}")
        except Exception as e:
            other += 1
            logger.error(f"Error sending message to user_id: {client['user_id']}, error: {e}")

    await asyncio.gather(*[notify_client(client) for client in clients])

    # Повертаємо статистику
    result = i18n.MESSAGING.TAX.RESULT(
        team_name=team_name,
        send=counter,
        users=len(clients),
        block=block,
        other=other
    )
    logger.info(f"Team '{team_name}': Sent={counter}, Blocked={block}, Other Errors={other}")
    return result
