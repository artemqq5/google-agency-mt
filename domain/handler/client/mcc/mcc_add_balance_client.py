import uuid

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.repositories.balances import BalanceRepository
from data.repositories.mcc_accesses import MCCAccessRepository
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.notification.admin_notify import NotificationAdmin
from domain.states.client.mcc.TopUpMCCClientState import TopUpMCCClientState
from presentation.keyboards.client.kb_mcc.kb_accounts import AddBalancClinetMCC, kb_back_detail_mcc

router = Router()


@router.callback_query(AddBalancClinetMCC.filter())
async def mcc_client_add_balance(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(TopUpMCCClientState.Value)
    await callback.message.edit_text(i18n.CLIENT.MCC.BALANCE.VALUE(), reply_markup=kb_back_detail_mcc)


@router.message(TopUpMCCClientState.Value)
async def send_request_add_mcc_balance(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    try:
        topup_value = int(message.text)
        if topup_value < 100 or topup_value > 10000:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.CLIENT.MCC.BALANCE.VALUE.ERROR(), reply_markup=kb_back_detail_mcc)
        return

    await state.update_data(value=topup_value)

    data = await state.get_data()
    await state.set_state(None)

    await message.answer(i18n.CLIENT.MCC.BALANCE.SUCCESS(), reply_markup=kb_back_detail_mcc)
    await NotificationAdmin.user_create_request(message.from_user.id, bot, i18n, data)



