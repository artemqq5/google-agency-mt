import subprocess
import time
import requests

from private_config import PATH_TO_MAIN_PY, BOT_TOKEN_CRUSH, TG_CHAT_ID


def send_error_to_admin(message):
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
    print('Starting mt google agency bot...')
    try:
        # Запуск процесу з контролем
        process = subprocess.run(
            ["python3.10", PATH_TO_MAIN_PY],
            check=True
        )
    except subprocess.CalledProcessError as e:
        # Обробка помилок виконання
        error_message = f"🚨 Bot process terminated with error: {e} 🚨"
        print(error_message)
        send_error_to_admin(error_message)
    except Exception as e:
        # Обробка несподіваних винятків
        error_message = f"🚨 Unexpected error: {e} 🚨"
        print(error_message)
        send_error_to_admin(error_message)

    # Перезапуск через 20 секунд
    print('Bot crashed. Restarting in 20 seconds...')
    send_error_to_admin('🚨 The bot crashed and will restart in 20 seconds. 🚨')
    time.sleep(20)
