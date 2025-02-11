import uuid

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.repositories.balances import BalanceRepository
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.notification.client_notify import NotificationTools
from domain.states.admin.mcc.TopUpBalanceAdminMCCState import TopUpBalanceAdminMCCState
from presentation.keyboards.admin.kb_teams.kb_mcc_access.kb_mcc_access import *

router = Router()


@router.callback_query(TopUpBalanceTeamMCC.filter())
async def topup_balance_mcc(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(TopUpBalanceAdminMCCState.Value)
    await callback.message.edit_text(
        text=i18n.TEAMS.MCC.BALANCE.VALUE(),
        reply_markup=kb_detail_team_mcc_back
    )


@router.message(TopUpBalanceAdminMCCState.Value)
async def set_value_topup(message: Message, state: FSMContext, i18n: I18nContext):
    try:
        topup_value = int(message.text)
    except ValueError as e:
        await message.answer(i18n.CLIENT.MCC.BALANCE.VALUE.ERROR(), reply_markup=kb_detail_team_mcc_back)
        return

    await state.update_data(value=topup_value)
    await message.answer(i18n.TEAMS.MCC.BALANCE.CONFIRMATION(value=topup_value), reply_markup=kb_topup_mcc_confirmation)


@router.callback_query(TopUpBalanceTeamMCCConfirmation.filter())
async def topup_balance_mcc_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()
    await callback.message.delete()
    await state.set_state(None)

    balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])
    team = TeamRepository().team_by_uuid(data['team_uuid'])

    # generate UUID for transaction
    transation_uuid = uuid.uuid4()

    if not TransactionRepository().add(
            value=data['value'],
            transaction_uuid=transation_uuid,
            balance_uuid=balance['balance_uuid'],
            mcc_uuid=data['mcc_uuid'],
            team_uuid=team['team_uuid'],
            team_name=team['team_name']
    ):
        await callback.message.edit_text(i18n.TEAMS.MCC.BALANCE.TOPUP.TRANSACTION.FAIL(
            error="can`t create transaction"), reply_markup=kb_detail_team_mcc_back
        )
        return

    if not BalanceRepository().add(data['value'], data['mcc_uuid'], team['team_uuid']):
        await callback.message.edit_text(i18n.TEAMS.MCC.BALANCE.TOPUP.TRANSACTION.FAIL(
            error="can`t update balance"), reply_markup=kb_detail_team_mcc_back
        )
        return

    await callback.message.edit_text(i18n.TEAMS.MCC.BALANCE.TOPUP.SUCCESS(), reply_markup=kb_detail_team_mcc_back)
    result = await NotificationTools.push_team(data, bot, i18n)
    await callback.message.answer(result)
