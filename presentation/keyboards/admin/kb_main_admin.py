from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_menu_admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.ADMIN.TEAMS()), KeyboardButton(text=L.ADMIN.MCC())],
    [KeyboardButton(text=L.ADMIN.MESSAGING()), KeyboardButton(text=L.ADMIN.PROFILE())],
], resize_keyboard=True)
