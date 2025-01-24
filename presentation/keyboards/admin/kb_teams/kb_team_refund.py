import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_teams.kb_teams import TeamRefund, BackTeamManage


class TeamRefundDetail(CallbackData, prefix="TeamRefundDetail"):
    account_uid: str


class NavigationTeamRefunds(CallbackData, prefix="NavigationTeamRefunds"):
    page: int


def kb_teams_refunds(refunds, current_page: int = 1):
    inline_kb = []

    # if items less then pages exist before -> Leave to 1 page
    if len(refunds) < (current_page * 5) - 4:
        current_page = 1

    total_pages = math.ceil(len(refunds) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(refunds))

    # load from db
    for i in range(start_index, end_index):
        status_emoji = "✅" if refunds[i]['status'] == 'success' else "⚙️"
        date_format = refunds[i]['created'].strftime("%d.%m.%y %H:%M")
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"{status_emoji} {refunds[i]['account_email']} | {date_format}",
                callback_data=TeamRefundDetail(account_uid=refunds[i]['account_uid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationTeamRefunds(page=current_page - 1).pack()
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
            callback_data=NavigationTeamRefunds(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(refunds) > 5:
        inline_kb.append(nav)

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=BackTeamManage().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


kb_back_refund_nav = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=TeamRefund().pack())]
])
