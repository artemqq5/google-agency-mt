import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_mcc.kb_mcc import BackMCCSManage


class CreateSubAccountAdmin(CallbackData, prefix="CreateSubAccountAdmin"):
    pass


class ShowDetailAccount(CallbackData, prefix="ShowDetailAccount"):
    account_uid: str


class NavigationAccount(CallbackData, prefix="NavigationAccount"):
    page: int


class SwitchGeneralMCC(CallbackData, prefix="SwitchGeneralMCC"):
    mcc_uuid: str


def kb_accounts_manage(accounts, mcc_uuid, current_page: int = 1):
    inline_kb = [
        [InlineKeyboardButton(
            text=L.MCC.GENERAL.SWITCH(),
            callback_data=SwitchGeneralMCC(mcc_uuid=mcc_uuid).pack()
        )],
        [InlineKeyboardButton(
            text=L.ADMIN.ACCOUNT.CREATE(),
            callback_data=CreateSubAccountAdmin().pack()
        )]
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


# back from crate new subaccount
kb_back_detail_mcc_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackAccountsManage().pack())],
])


class SkipTeamUUIDAccountCreate(CallbackData, prefix="SkipTeamUUIDAccountCreate"):
    pass


# back from crate new subaccount team skip
kb_team_uuid_skip_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.ACCOUNT.CREATE.TEAM.SKIP(), callback_data=SkipTeamUUIDAccountCreate().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackAccountsManage().pack())],
])


class ChangeTeamAccount(CallbackData, prefix="ChangeTeamAccount"):
    pass


class TopUpAccount(CallbackData, prefix="TopUpAccount"):
    pass


class TopUpAccountConfirmation(CallbackData, prefix="TopUpAccountConfirmation"):
    pass


class ChangeEmailAccount(CallbackData, prefix="ChangeEmailAccount"):
    pass


class RefundAccount(CallbackData, prefix="RefundAccount"):
    pass


class RefundAccountConfirmation(CallbackData, prefix="RefundAccountConfirmation"):
    pass


# topup, refund, change email, change team
kb_back_accounts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.ACCOUNT.CHANGE_TEAM(), callback_data=ChangeTeamAccount().pack())],
    [InlineKeyboardButton(text=L.ADMIN.ACCOUNT.TOPUP(), callback_data=TopUpAccount().pack())],
    [InlineKeyboardButton(text=L.ADMIN.ACCOUNT.CHANGE_EMAIL(), callback_data=ChangeEmailAccount().pack())],
    [InlineKeyboardButton(text=L.ADMIN.ACCOUNT.REFUND(), callback_data=RefundAccount().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackAccountsManage().pack())]
])


class ShowDetailAccountBack(CallbackData, prefix="ShowDetailAccountBack"):
    pass


kb_back_account = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailAccountBack().pack())],
])


kb_account_topup_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.ACCOUNT.TOPUP.CONFIRMATION(), callback_data=TopUpAccountConfirmation().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailAccountBack().pack())],
])

kb_account_refund_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.CLIENT.ACCOUNT.REFUND.CONFIRMATION(), callback_data=RefundAccountConfirmation().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailAccountBack().pack())],
])

# Back to mcc managment
# class BackMCCManage(CallbackData, prefix="BackMCCManage"):
#     pass


# kb_back_mcc = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text=L.BACK(), callback_data=BackMCCManage().pack())]
# ])
