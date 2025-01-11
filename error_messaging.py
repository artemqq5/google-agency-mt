import requests

from private_config import BOT_TOKEN_CRUSH, TG_CHAT_ID


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