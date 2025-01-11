import os
import time

import requests

from private_config import PATH_TO_MAIN_PY, BOT_TOKEN_CRUSH, TG_CHAT_ID


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN_CRUSH}/sendMessage"
    payload = {
        "chat_id": TG_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Error message sent successfully.")
        else:
            print(f"Failed to send message. Response: {response.text}")
    except Exception as err:
        print(f"Exception while sending message: {err}")


while True:
    print('start mt google agency bot')
    try:
        os.system(f"python3.10 {PATH_TO_MAIN_PY}")
    except Exception as e:
        error_message = f'Exception in start: {e}'
        print(error_message)
        send_telegram_message(error_message)

    print('crash')
    send_telegram_message('🚨The bot crashed and will restart in 20 seconds. 🚨')
    time.sleep(20)
