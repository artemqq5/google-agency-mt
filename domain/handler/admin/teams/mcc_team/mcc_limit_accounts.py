from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.mcc_accesses import MCCAccessRepository
from domain.states.admin.team.AccountsMCCLimitState import AccountsMCCLimitState
from presentation.keyboards.admin.kb_teams.kb_mcc_access.kb_mcc_access import AccountsMCCLimit, kb_detail_team_mcc_back
from presentation.keyboards.admin.kb_teams.kb_mcc_access.kb_share_mcc import kb_share_mcc_back

router = Router()


@router.callback_query(AccountsMCCLimit.filter())
async def edit_accounts_mcc_limit(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(AccountsMCCLimitState.Limit)

    await callback.message.edit_text(
        text=i18n.TEAMS.MCC.ACCOUNTS.LIMIT.VALUE(),
        reply_markup=kb_detail_team_mcc_back
    )


@router.message(AccountsMCCLimitState.Limit)
async def save_accounts_limit(message: Message, state: FSMContext, i18n: I18nContext):
    try:
        mcc_limit = int(message.text)
        if mcc_limit < 0 or mcc_limit > 999:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.TEAMS.MCC.ACCOUNTS.LIMIT.VALUE_ERROR(), reply_markup=kb_detail_team_mcc_back)
        return

    data = await state.get_data()

    if MCCAccessRepository().mcc_access(data['mcc_uuid'], data['team_uuid'])['account_available'] == mcc_limit:
        await message.answer(i18n.TEAMS.MCC.ACCOUNTS.LIMIT.VALUE_DUBL(limit=mcc_limit), reply_markup=kb_detail_team_mcc_back)
        return

    await state.set_state(None)

    if not MCCAccessRepository().change_limit_by_uuid(mcc_limit, data['mcc_uuid'], data['team_uuid']):
        await message.answer(i18n.TEAMS.MCC.ACCOUNTS.LIMIT.FAIL(), reply_markup=kb_share_mcc_back)
        return

    await message.answer(i18n.TEAMS.MCC.ACCOUNTS.LIMIT.SUCCESS(limit=mcc_limit), reply_markup=kb_detail_team_mcc_back)
