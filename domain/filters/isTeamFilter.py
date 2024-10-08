from aiogram.filters import BaseFilter
from aiogram.types import Message

from data.repositories.accesses import AccessRepository
from data.repositories.teams import TeamRepository


class IsTeamFilter(BaseFilter):

    def __init__(self, is_has_team: bool = True):
        self.is_has_team = is_has_team

    async def __call__(self, message: Message):
        try:
            access = AccessRepository().access_by_user_id(message.from_user.id)
            team = TeamRepository().team_by_uuid(access['team_uuid'])
        except Exception as _:
            team = False

        return team if self.is_has_team else not team
