import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class AddNewMCC(CallbackData, prefix="AddNewMCC"):
    pass


class ShowDetailMCC(CallbackData, prefix="ShowDetailMCC"):
    mcc_uuid: str


class NavigationMCC(CallbackData, prefix="NavigationMCC"):
    page: int


def kb_mccs_manage(mcc_list, current_page: int = 1):
    # create new team
    inline_kb = [[InlineKeyboardButton(
        text=L.MCC.ADD(),
        callback_data=AddNewMCC().pack()
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
                callback_data=ShowDetailMCC(mcc_uuid=mcc_list[i]['mcc_uuid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationMCC(page=current_page - 1).pack()
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
            callback_data=NavigationMCC(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(mcc_list) > 5:
        inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


# Back to mccs managment
class BackMCCSManage(CallbackData, prefix="BackMCCSManage"):
    pass


kb_back_mccs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMCCSManage().pack())]
])


# Back to mcc managment
class BackMCCManage(CallbackData, prefix="BackMCCManage"):
    pass


kb_back_mcc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMCCManage().pack())]
])


# Delete team
# class TeamDelete(CallbackData, prefix="TeamDelete"):
#     pass


# Team accesses managment/back
# class TeamAccessesBack(CallbackData, prefix="TeamAccessesBack"):
#     pass


# class TeamMCCLimit(CallbackData, prefix="TeamMCCLimit"):
#     pass


kb_back_to_team = InlineKeyboardMarkup(inline_keyboard=[
    # [InlineKeyboardButton(text=L.TEAMS.ACCESS(), callback_data=TeamAccessesBack().pack())],
    # [InlineKeyboardButton(text=L.TEAMS.MCC.LIMIT(), callback_data=TeamMCCLimit().pack())],
    # [InlineKeyboardButton(text=L.TEAMS.DELETE(), callback_data=TeamDelete().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMCCSManage().pack())]
])
