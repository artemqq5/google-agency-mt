import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_teams.kb_teams import BackTeamManage, ManageMCCSTeam


class ShareMCCTeam(CallbackData, prefix="ShareMCCTeam"):
    pass


class ShowDetailMCCTeam(CallbackData, prefix="ShowDetailMCCTeam"):
    mcc_uuid: str


class NavigationMCCTeam(CallbackData, prefix="NavigationMCCTeam"):
    page: int


def kb_mccs_team_manage(mcc_list, current_page: int = 1):
    # share new mcc for team
    inline_kb = [[InlineKeyboardButton(
        text=L.TEAMS.MCC.SHARE(),
        callback_data=ShareMCCTeam().pack()
    )]]

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
                callback_data=ShowDetailMCCTeam(mcc_uuid=mcc_list[i]['mcc_uuid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationMCCTeam(page=current_page - 1).pack()
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
            callback_data=NavigationMCCTeam(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(mcc_list) > 5:
        inline_kb.append(nav)

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=BackTeamManage().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class ShowDetailMCCTeamBack(CallbackData, prefix="ShowDetailMCCTeamBack"):
    pass


class ReShareMCC(CallbackData, prefix="ReShareMCC"):
    pass


class ReShareConfirmationMCC(CallbackData, prefix="ReShareConfirmationMCC"):
    pass


class AccountsMCCLimit(CallbackData, prefix="AccountsMCCLimit"):
    pass


class TopUpBalanceTeamMCC(CallbackData, prefix="TopUpBalanceTeamMCC"):
    pass


class TopUpBalanceTeamMCCConfirmation(CallbackData, prefix="TopUpBalanceTeamMCCConfirmation"):
    pass


kb_detail_team_mcc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.TEAMS.MCC.BALANCE.ADD(), callback_data=TopUpBalanceTeamMCC().pack())],
    [InlineKeyboardButton(text=L.TEAMS.MCC.RESHARE(), callback_data=ReShareMCC().pack())],
    [InlineKeyboardButton(text=L.TEAMS.MCC.ACCOUNTS.LIMIT(), callback_data=AccountsMCCLimit().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ManageMCCSTeam().pack())]
])


kb_reshare_mcc_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.TEAMS.MCC.RESHARE(), callback_data=ReShareConfirmationMCC().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailMCCTeamBack().pack())]
])

kb_topup_mcc_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.TEAMS.MCC.BALANCE.CREATE.TRANSACTION(), callback_data=TopUpBalanceTeamMCCConfirmation().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailMCCTeamBack().pack())]
])

kb_detail_team_mcc_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=ShowDetailMCCTeamBack().pack())]
])

kb_team_mccs_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=ManageMCCSTeam().pack())]
])
