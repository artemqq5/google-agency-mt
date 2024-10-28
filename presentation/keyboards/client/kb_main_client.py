from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.constants import FAQ_LINK

kb_menu_client = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.CLIENT.ACCOUNTS())],
    [KeyboardButton(text=L.FAQ())],
], resize_keyboard=True)


kb_faq = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.OPEN(), url=FAQ_LINK)],
])


