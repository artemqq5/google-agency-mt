import uuid

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.accesses import AccessRepository
from data.repositories.teams import TeamRepository
from presentation.keyboards.admin.kb_teams.kb_accesses.kb_team_access import CreateNewAccessTeam, \
    kb_back_to_team_accesses, CreateAccessConfirmation, kb_create_access
from private_config import LINK_TO_BOT

router = Router()


@router.callback_query(CreateNewAccessTeam.filter())
async def create_team_access(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    team = TeamRepository().team_by_uuid(data['team_uuid'])
    await callback.message.edit_text(
        text=i18n.TEAMS.ACCESS.CREATE.CONFIRMANTION(team=team['team_name']),
        reply_markup=kb_create_access
    )


@router.callback_query(CreateAccessConfirmation.filter())
async def confirmation_create_access(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    team = TeamRepository().team_by_uuid(data['team_uuid'])

    # generate UUID for team access
    access_uuid = uuid.uuid4()

    if not AccessRepository().generate_accesss(access_uuid, team['team_uuid'], team['team_name']):
        await callback.message.edit_text(
            i18n.TEAMS.ACCESS.CREATE.FAIL(team=team['team_name']),
            reply_markup=kb_back_to_team_accesses
        )
        return

    await callback.message.edit_text(
        i18n.TEAMS.ACCESS.CREATE.SUCCESS(
            team=team['team_name'],
            deeplink=f"{LINK_TO_BOT}?start={access_uuid}"
        ),
        reply_markup=kb_back_to_team_accesses
    )
