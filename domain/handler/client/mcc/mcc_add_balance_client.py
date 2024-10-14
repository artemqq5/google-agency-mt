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
from domain.states.client.TopUpBalanceClientMCCState import TopUpBalanceClientMCCState
from presentation.keyboards.client.kb_mcc.kb_accounts import AddBalancClinetMCC, kb_back_accounts_client

router = Router()


@router.callback_query(AddBalancClinetMCC.filter())
async def mcc_client_add_balance(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(TopUpBalanceClientMCCState.Value)
    await callback.message.edit_text(i18n.CLIENT.MCC.BALANCE.VALUE(), reply_markup=kb_back_accounts_client)


@router.message(TopUpBalanceClientMCCState.Value)
async def send_transaction_add_mcc_balance(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    try:
        topup_value = int(message.text)
        if topup_value < 100 or topup_value > 9999:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.CLIENT.MCC.BALANCE.VALUE.ERROR(), reply_markup=kb_back_accounts_client)
        return

    data = await state.get_data()
    await state.set_state(None)

    balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])
    team = TeamRepository().team_by_uuid(data['team_uuid'])

    # generate UUID for transaction
    transation_uuid = uuid.uuid4()

    if not TransactionRepository().add(
            value=topup_value,
            transaction_uuid=transation_uuid,
            balance_uuid=balance['balance_uuid'],
            mcc_uuid=data['mcc_uuid'],
            team_uuid=team['team_uuid'],
            team_name=team['team_name']
    ):
        await message.answer(i18n.CLIENT.MCC.BALANCE.FAIL(), reply_markup=kb_back_accounts_client)
        return

    await message.answer(i18n.CLIENT.MCC.BALANCE.SUCCESS(), reply_markup=kb_back_accounts_client)
    await NotificationAdmin.user_create_transaction(message.from_user.id, bot, i18n, transation_uuid)

