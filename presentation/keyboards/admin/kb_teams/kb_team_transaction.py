import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from presentation.keyboards.admin.kb_teams.kb_teams import TeamTransaction, TeamTransactionAccount, TeamTransactionMCC


########################################## Team Transaction MCC ##########################################

class TeamTransactionMCCDetail(CallbackData, prefix="TeamTransactionMCCDetail"):
    transaction_uuid: str


class NavigationeamTransactionMCC(CallbackData, prefix="NavigationeamTransactionMCC"):
    page: int


def kb_teams_transaction_mcc(transactions, current_page: int = 1):
    inline_kb = []

    # if items less then pages exist before -> Leave to 1 page
    if len(transactions) < (current_page * 5) - 4:
        current_page = 1

    total_pages = math.ceil(len(transactions) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(transactions))

    # load from db
    for i in range(start_index, end_index):
        mcc = MCCRepository().mcc_by_uuid(transactions[i]['mcc_uuid'])
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"#{transactions[i]['id']} | {transactions[i]['value']}$ | {mcc['mcc_name']}",
                callback_data=TeamTransactionMCCDetail(transaction_uuid=transactions[i]['transaction_uuid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationeamTransactionMCC(page=current_page - 1).pack()
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
            callback_data=NavigationeamTransactionMCC(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(transactions) > 5:
        inline_kb.append(nav)

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=TeamTransaction().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


kb_transaction_mcc_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=TeamTransactionMCC().pack())]
])


########################################## Team Transaction SUB ##########################################
class TeamTransactionSUBDetail(CallbackData, prefix="TeamTransactionSUBDetail"):
    transaction_uuid: str


class NavigationeamTransactionSUB(CallbackData, prefix="NavigationeamTransactionSUB"):
    page: int


def kb_teams_transaction_sub(transactions, current_page: int = 1):
    inline_kb = []

    # if items less then pages exist before -> Leave to 1 page
    if len(transactions) < (current_page * 5) - 4:
        current_page = 1

    total_pages = math.ceil(len(transactions) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(transactions))

    # load from db
    for i in range(start_index, end_index):
        sub = SubAccountRepository().account_by_uid(transactions[i]['sub_account_uid'])
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"#{transactions[i]['id']} | {transactions[i]['value']}$ | {sub['account_email']}",
                callback_data=TeamTransactionSUBDetail(transaction_uuid=transactions[i]['transaction_uuid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationeamTransactionSUB(page=current_page - 1).pack()
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
            callback_data=NavigationeamTransactionSUB(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(transactions) > 5:
        inline_kb.append(nav)

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=TeamTransaction().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


kb_transaction_sub_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=TeamTransactionAccount().pack())]
])
