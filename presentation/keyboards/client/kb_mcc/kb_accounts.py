import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.client.kb_mcc.kb_mcc import BackMCCSManageClient


class AddBalancClinetMCC(CallbackData, prefix="AddBalancClinetMCC"):
    pass


class CreateSubAccountClient(CallbackData, prefix="CreateSubAccountClient"):
    pass


class ShowDetailAccountClient(CallbackData, prefix="ShowDetailAccountClient"):
    account_uid: str


class NavigationAccountClient(CallbackData, prefix="NavigationAccountClient"):
    page: int


def kb_accounts_manage_client(accounts, current_page: int = 1):
    # add balance
    inline_kb = [
        [InlineKeyboardButton(text=L.CLIENT.MCC.BALANCE.ADD(), callback_data=AddBalancClinetMCC().pack())],
        [InlineKeyboardButton(text=L.CLIENT.ACCOUNT.CREATE(), callback_data=CreateSubAccountClient().pack())]
    ]

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
                callback_data=ShowDetailAccountClient(account_uid=accounts[i]['account_uid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationAccountClient(page=current_page - 1).pack()
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
            callback_data=NavigationAccountClient(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(accounts) > 5:
        inline_kb.append(nav)

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=BackMCCSManageClient().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


# Back to mccs managment
class ShowDetailClientMCCBack(CallbackData, prefix="ShowDetailClientMCCBack"):
    pass


class ChangeEmailClientAccount(CallbackData, prefix="ChangeEmailClientAccount"):
    pass


class RefoundClientAccount(CallbackData, prefix="RefoundClientAccount"):
    pass


class RefoundClientAccountConfirmation(CallbackData, prefix="RefoundClientAccountConfirmation"):
    pass


class TopUpClientAccount(CallbackData, prefix="TopUpClientAccount"):
    pass


class TopUpClientAccountConfirmation(CallbackData, prefix="TopUpClientAccountConfirmation"):
    pass


kb_back_accounts_client = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.CLIENT.ACCOUNT.TOPUP(), callback_data=TopUpClientAccount().pack())],
    [InlineKeyboardButton(text=L.CLIENT.ACCOUNT.CHANGE_EMAIL(), callback_data=ChangeEmailClientAccount().pack())],
    [InlineKeyboardButton(text=L.CLIENT.ACCOUNT.REFOUND(), callback_data=RefoundClientAccount().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailClientMCCBack().pack())],
])


class ShowDetailAccountClientBack(CallbackData, prefix="ShowDetailAccountClientBack"):
    pass


kb_back_detail_mcc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailClientMCCBack().pack())],
])

kb_back_detail_account = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailAccountClientBack().pack())],
])

kb_back_account_topup_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.CLIENT.ACCOUNT.TOPUP.CONFIRMATION(),
                          callback_data=TopUpClientAccountConfirmation().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailAccountClientBack().pack())],
])

kb_back_account_refound_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.CLIENT.ACCOUNT.REFOUND.CONFIRMATION(),
                          callback_data=RefoundClientAccountConfirmation().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailAccountClientBack().pack())],
])

# Back to mcc managment
# class BackMCCManage(CallbackData, prefix="BackMCCManage"):
#     pass


# kb_back_mcc = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text=L.BACK(), callback_data=BackMCCManage().pack())]
# ])
