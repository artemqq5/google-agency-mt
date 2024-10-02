import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class CreateNewTeam(CallbackData, prefix="CreateNewTeam"):
    pass


class TeamShowDetail(CallbackData, prefix="TeamShowDetail"):
    team_uuid: str


class NavigationTeams(CallbackData, prefix="NavigationTeams"):
    page: int


def kb_teams_manage(teams, current_page: int = 1):
    # create new team
    inline_kb = [[InlineKeyboardButton(
        text=L.TEAMS.CREATE(),
        callback_data=CreateNewTeam().pack()
    )]]

    # if items less then pages exist before -> Leave to 1 page
    if len(teams) < (current_page * 5)-4:
        current_page = 1

    total_pages = math.ceil(len(teams) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(teams))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"#{teams[i]['team_id']} | {teams[i]['team_name']}",
                callback_data=TeamShowDetail(team_uuid=teams[i]['team_uuid']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=NavigationTeams(page=current_page - 1).pack()
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
            callback_data=NavigationTeams(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    if len(teams) > 5:
        inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


# Back to teams managment
class BackTeamsManage(CallbackData, prefix="BackTeamsManage"):
    pass


kb_back_teams = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackTeamsManage().pack())]
])


# Back to team managment
class BackTeamManage(CallbackData, prefix="BackTeamManage"):
    pass


kb_back_to_team = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackTeamManage().pack())]
])


# Team accesses managment/back
class TeamAccessesBack(CallbackData, prefix="TeamAccessesBack"):
    pass


kb_team_detail = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.TEAMS.ACCESS(), callback_data=TeamAccessesBack().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackTeamsManage().pack())]
])
