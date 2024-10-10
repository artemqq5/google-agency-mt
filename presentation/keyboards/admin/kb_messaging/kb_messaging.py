import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class SkipMediaMessaging(CallbackData, prefix="SkipMediaMessaging"):
    pass


class SendMessageMessaging(CallbackData, prefix="SendMessageMessaging"):
    pass


kb_media_skip = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.SKIP(), callback_data=SkipMediaMessaging().pack())]
])


kb_media_send = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.MESSAGING.SEND(), callback_data=SendMessageMessaging().pack())]
])

