import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_mcc.kb_mcc import BackMCCSManage


# class AddNewMCC(CallbackData, prefix="AddNewMCC"):
#     pass


class ShowDetailAccount(CallbackData, prefix="ShowDetailAccount"):
    account_uid: str


class NavigationAccount(CallbackData, prefix="NavigationAccount"):
    page: int


def kb_accounts_manage(accounts, current_page: int = 1):
    # create new account
    # inline_kb = [[InlineKeyboardButton(
    #     text=L.MCC.ADD(),
    #     callback_data=AddNewMCC().pack()
    # )]]

    inline_kb = []

    # if items less then pages exist before -> Leave to 1 page
    if len(accounts) < (current_page * 5) - 4:
        current_page = 1

    total_pages = math.ceil(len(accounts) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(accounts))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"{accounts[i]['account_email']}",
                callback_data=ShowDetailAccount(account_uid=accounts[i]['account_uid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationAccount(page=current_page - 1).pack()
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
            callback_data=NavigationAccount(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(accounts) > 5:
        inline_kb.append(nav)

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=BackMCCSManage().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


# Back to mccs managment
class BackAccountsManage(CallbackData, prefix="BackAccountsManage"):
    pass


kb_back_accounts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackAccountsManage().pack())]
])


# Back to mcc managment
# class BackMCCManage(CallbackData, prefix="BackMCCManage"):
#     pass


# kb_back_mcc = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text=L.BACK(), callback_data=BackMCCManage().pack())]
# ])

