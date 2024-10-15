from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from domain.states.client.account.TopUpAccountClientState import TopUpAccountClientState
from presentation.keyboards.client.kb_mcc.kb_accounts import TopUpClientAccount, kb_back_detail_account, \
    TopUpClientAccountConfirmation, kb_back_account_topup_confirmation

router = Router()


@router.callback_query(TopUpClientAccount.filter())
async def topup_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(TopUpAccountClientState.Value)
    await callback.message.edit_text(i18n.CLIENT.ACCOUNT.TOPUP.VALUE(), reply_markup=kb_back_detail_account)


@router.message(TopUpAccountClientState.Value)
async def topup_value_save(message: Message, state: FSMContext, i18n: I18nContext):
    try:
        topup_value = int(message.text)
        if topup_value < 100 or topup_value > 10000:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.CLIENT.MCC.BALANCE.VALUE.ERROR(), reply_markup=kb_back_detail_account)
        return

    await state.update_data(value=topup_value)
    await message.answer(i18n.CLIENT.ACCOUNT.TOPUP.WARNING(value=topup_value), reply_markup=kb_back_account_topup_confirmation)


@router.callback_query(TopUpClientAccountConfirmation.filter())
async def topup_account_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    pass
