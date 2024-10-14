from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.sub_transactions import SubTransactionRepository
from presentation.keyboards.admin.kb_teams.kb_team_transaction import NavigationeamTransactionSUB, \
    kb_teams_transaction_sub, TeamTransactionSUBDetail, kb_transaction_sub_back
from presentation.keyboards.admin.kb_teams.kb_teams import TeamTransactionAccount

router = Router()


@router.callback_query(TeamTransactionAccount.filter())
async def team_transactions_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    transactions_account = SubTransactionRepository().transactions_by_team(data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.TRANSACTIONS.SUB(),
        reply_markup=kb_teams_transaction_sub(transactions_account, data.get('last_page_transaction_account', 1))
    )


@router.callback_query(NavigationeamTransactionSUB.filter())
async def transactions_account_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()
    transactions_account = SubTransactionRepository().transactions_by_team(data['team_uuid'])

    await state.update_data(last_page_transaction_mcc=page)

    await callback.message.edit_reply_markup(reply_markup=kb_teams_transaction_sub(transactions_account, page))


@router.callback_query(TeamTransactionSUBDetail.filter())
async def transaction_account_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    transaction_uuid = callback.data.split(":")[1]
    transaction = SubTransactionRepository().transaction(transaction_uuid)
    mcc = MCCRepository().mcc_by_uuid(transaction['mcc_uuid'])
    account = SubAccountRepository().account_by_uid(transaction['sub_account_uid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.TRANSACTIONS.SUB.DETAIL(
            id_transaction=transaction['id'],
            uuid_transaction=transaction['transaction_uuid'],
            mcc_name=mcc['mcc_name'],
            account_email=account['account_email'],
            value=transaction['value'],
            date=str(transaction['created'])
        ),
        reply_markup=kb_transaction_sub_back
    )
