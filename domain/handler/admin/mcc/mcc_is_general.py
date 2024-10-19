from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.mcc import MCCRepository
from presentation.keyboards.admin.kb_mcc.kb_accounts import SwitchGeneralMCC

router = Router()


@router.callback_query(SwitchGeneralMCC.filter())
async def mcc_general_switch(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    mcc_uuid = callback.data.split(":")[1]
    mcc = MCCRepository().mcc_by_uuid(mcc_uuid)

    MCCRepository().update_general(mcc_uuid, not bool(mcc['is_general']))

    from domain.handler.admin.mcc.nav_mcc import mcc_detail
    await mcc_detail(callback, i18n, state)
