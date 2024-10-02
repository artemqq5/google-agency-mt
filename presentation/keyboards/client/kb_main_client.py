from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_client = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.CLIENT.ACCOUNTS()), KeyboardButton(text=L.CLIENT.PROFILE())]
], resize_keyboard=True)
