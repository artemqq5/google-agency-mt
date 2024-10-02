import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.teams.kb_teams import BackTeamManage, TeamAccessesBack


class CreateNewAccessTeam(CallbackData, prefix="CreateNewAccessTeam"):
    pass


class AccessTeamShowDetail(CallbackData, prefix="AccessTeamShowDetail"):
    access_uuid: str


class NavigationAccessTeam(CallbackData, prefix="NavigationAccessTeam"):
    page: int


def kb_access_teams_manage(access_team, current_page: int = 1):
    # create new access team
    inline_kb = [[InlineKeyboardButton(
        text=L.TEAMS.ACCESS.CREATE(),
        callback_data=CreateNewAccessTeam().pack()
    )]]

    # if items less then pages exist before -> Leave to 1 page
    if len(access_team) < (current_page * 5)-4:
        current_page = 1

    total_pages = math.ceil(len(access_team) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(access_team))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"{access_team[i]['access_uuid']}",
                callback_data=AccessTeamShowDetail(access_uuid=access_team[i]['access_uuid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationAccessTeam(page=current_page - 1).pack()
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
            callback_data=NavigationAccessTeam(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(access_team) > 5:
        inline_kb.append(nav)

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=BackTeamManage().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class CreateAccessConfirmation(CallbackData, prefix="CreateAccessConfirmation"):
    pass


kb_back_to_team_accesses = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=TeamAccessesBack().pack())],
])


kb_back_to_team_accesses_with_create = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=TeamAccessesBack().pack())],
    [InlineKeyboardButton(text=L.TEAMS.ACCESS.CREATE(), callback_data=CreateAccessConfirmation().pack())],
])
