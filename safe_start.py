import os
import time

from error_messaging import send_error_to_admin
from private_config import PATH_TO_MAIN_PY

while True:
    print('start mt google agency bot')
    try:
        os.system(f"python3.10 {PATH_TO_MAIN_PY}")
    except Exception as e:
        error_message = f'Exception in start: {e}'
        print(error_message)
        send_error_to_admin(error_message)

    print('crash')
    send_error_to_admin('🚨The bot crashed and will restart in 20 seconds. 🚨')
    time.sleep(20)
