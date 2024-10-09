import os
import time

from private_config import PATH_TO_MAIN_PY

while True:
    print('start mt google agency bot')
    try:
        os.system(f"python3.10 {PATH_TO_MAIN_PY}")
    except Exception as e:
        print(f'exception in start: {e}')
    print('crash')
    time.sleep(20)
