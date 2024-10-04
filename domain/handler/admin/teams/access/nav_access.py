from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.accesses import AccessRepository
from data.repositories.users import UserRepository
from domain.handler.admin.teams.access import create_access, delete_access
from presentation.keyboards.admin.kb_teams.kb_accesses.kb_delete_access import kb_team_access_manage
from presentation.keyboards.admin.kb_teams.kb_accesses.kb_team_access import NavigationAccessTeam, \
    kb_access_teams_manage, \
    AccessTeamShowDetail, kb_back_to_team_accesses
from presentation.keyboards.admin.kb_teams.kb_teams import kb_teams_manage, TeamAccessesBack
from private_config import LINK_TO_BOT

router = Router()

router.include_routers(
    create_access.router,
    delete_access.router
)


@router.callback_query(TeamAccessesBack.filter())
async def accesses_team_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    accesses_team = AccessRepository().accesses_by_team_uuid(data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.ACCESS(),
        reply_markup=kb_access_teams_manage(accesses_team, data.get('last_page_team_accesses', 1))
    )


@router.callback_query(NavigationAccessTeam.filter())
async def accesses_teams_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()
    accesses_team = AccessRepository().accesses_by_team_uuid(data['team_uuid'])

    await state.update_data(last_page_team_accesses=page)

    await callback.message.edit_reply_markup(reply_markup=kb_teams_manage(accesses_team, page))


@router.callback_query(AccessTeamShowDetail.filter())
async def access_team_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    access_uuid = callback.data.split(":")[1]
    access_team = AccessRepository().access_by_uuid(access_uuid)
    user = UserRepository().user(access_team['user_id'])
    user = {} if not user else user

    await state.update_data(access_uuid=access_uuid)

    await callback.message.edit_text(
        text=i18n.TEAMS.ACCESS.DETAIL(
            team=access_team['team_name'],
            deeplink=f"{LINK_TO_BOT}?start={access_uuid}",
            user_id=str(user.get('user_id', 'None')),
            username=str(user.get('username', 'None')),
            firstname=str(user.get('firstname', 'None')),
            lastname=str(user.get('lastname', 'None')),
            created=str(access_team['created']),
            activated=str(access_team['activated'])
        ),
        reply_markup=kb_team_access_manage
    )


