import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_teams.kb_mcc_access.kb_mcc_access import ShareMCCTeam
from presentation.keyboards.admin.kb_teams.kb_teams import BackTeamManage, ManageMCCSTeam


class ShowDetailMCCTeamShare(CallbackData, prefix="ShowDetailMCCTeamShare"):
    mcc_uuid: str


class NavigationMCCTeamShare(CallbackData, prefix="NavigationMCCTeamShare"):
    page: int


def kb_mccs_team_share(mcc_list, current_page: int = 1):
    inline_kb = []

    # if items less then pages exist before -> Leave to 1 page
    if len(mcc_list) < (current_page * 5) - 4:
        current_page = 1

    total_pages = math.ceil(len(mcc_list) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(mcc_list))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"{mcc_list[i]['mcc_name']}",
                callback_data=ShowDetailMCCTeamShare(mcc_uuid=mcc_list[i]['mcc_uuid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationMCCTeamShare(page=current_page - 1).pack()
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
            callback_data=NavigationMCCTeamShare(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(mcc_list) > 5:
        inline_kb.append(nav)

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=ManageMCCSTeam().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class ShareMCC(CallbackData, prefix="ShareMCC"):
    pass


kb_detail_share_mcc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.TEAMS.MCC.SHARE(), callback_data=ShareMCC().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ManageMCCSTeam().pack())],
])

kb_share_mcc_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShareMCCTeam().pack())],
])
