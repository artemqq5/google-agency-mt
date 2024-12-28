import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.repositories.taxes import TaxRepository


class TransactionTaxDetail(CallbackData, prefix="TransactionTaxDetail"):
    transaction_uuid: str


class NavigationTransactionTax(CallbackData, prefix="NavigationTransactionTax"):
    page: int


def kb_transaction_tax(transactions, current_page: int = 1):
    inline_kb = []

    # if items less then pages exist before -> Leave to 1 page
    if len(transactions) < (current_page * 10) - 9:
        current_page = 1

    total_pages = math.ceil(len(transactions) / 10)
    start_index = (current_page - 1) * 10
    end_index = min(start_index + 10, len(transactions))

    # load from db
    for i in range(start_index, end_index):
        sub = TaxRepository().get(transactions[i]['transaction_uuid'])
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"#{transactions[i]['id']} | {transactions[i]['mcc_name']} | {transactions[i]['amount']}$ | {sub['email']}",
                callback_data=TransactionTaxDetail(transaction_uuid=transactions[i]['transaction_uuid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationTransactionTax(page=current_page - 1).pack()
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
            callback_data=NavigationTransactionTax(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(transactions) > 10:
        inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class TransactionTax(CallbackData, prefix="TransactionTax"):
    pass


kb_transaction_tax_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=TransactionTax().pack())]
])
