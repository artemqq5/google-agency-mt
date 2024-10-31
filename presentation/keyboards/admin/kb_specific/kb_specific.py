import math

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


class SpecificMainBack(CallbackData, prefix="SpecificMainBack"):
    pass


kb_specific_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=SpecificMainBack().pack())]
])

# confirmation load accounts
kb_load_account_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.SPECIFIC.LOAD.CONFIRMATION(), callback_data=SpecificLoadAccountsConfirmation().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=SpecificMainBack().pack())]
])


class SpecificChoiceMCC(CallbackData, prefix="SpecificChoiceMCC"):
    mcc_uuid: str


class SpecificChoiceMCC_Navigation(CallbackData, prefix="SpecificChoiceMCC_Navigation"):
    page: int


def kb_specific_choice_mcc(mccs, current_page: int = 1):
    inline_kb = []

    # if items less then pages exist before -> Leave to 1 page
    if len(mccs) < (current_page * 10) - 9:
        current_page = 1

    total_pages = math.ceil(len(mccs) / 10)
    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(mccs))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"{mccs[i]['mcc_name']}",
                callback_data=SpecificChoiceMCC(mcc_uuid=mccs[i]['mcc_uuid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=SpecificChoiceMCC_Navigation(page=current_page - 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data="None"
        ))

    nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

    if current_page < total_pages:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data=SpecificChoiceMCC_Navigation(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(mccs) > 10:
        inline_kb.append(nav)

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=SpecificMainBack().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)

