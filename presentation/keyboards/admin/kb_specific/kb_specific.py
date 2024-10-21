from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class SpecificLoadAccounts(CallbackData, prefix="SpecificLoadAccounts"):
    pass


class SpecificLoadAccountsConfirmation(CallbackData, prefix="SpecificLoadAccountsConfirmation"):
    pass


kb_specific_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.SPECIFIC.LOAD(), callback_data=SpecificLoadAccounts().pack())]
])


class SpecificMain(CallbackData, prefix="SpecificMain"):
    pass


kb_specific_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=SpecificMain().pack())]
])

# confirmation load accounts
kb_load_account_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.SPECIFIC.LOAD.CONFIRMATION(), callback_data=SpecificLoadAccountsConfirmation().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=SpecificMain().pack())]
])
