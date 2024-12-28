from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.taxes import TaxRepository
from presentation.keyboards.client.kb_taxes.kb_taxes import *

router = Router()


@router.callback_query(TransactionTax.filter())
async def client_transactions_tax(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    transactions_tax = TaxRepository().taxes_by_team(data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.TRANSACTIONS.TAX(),
        reply_markup=kb_transaction_tax(transactions_tax, data.get('last_page_transaction_tax', 1))
    )


@router.callback_query(NavigationTransactionTax.filter())
async def client_transactions_tax_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()
    transactions_tax = TaxRepository().taxes_by_team(data['team_uuid'])

    await state.update_data(last_page_transaction_tax=page)

    await callback.message.edit_reply_markup(reply_markup=kb_transaction_tax(transactions_tax, page))


@router.callback_query(TransactionTaxDetail.filter())
async def client_transaction_tax_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    transaction_uuid = callback.data.split(":")[1]
    transaction = TaxRepository().get(transaction_uuid)

    await callback.message.edit_text(
        text=i18n.CLIENT.TRANSACTIONS.TAX.DETAIL(
            id_transaction=transaction['id'],
            uuid_transaction=transaction['transaction_uuid'],
            mcc_name=transaction['mcc_name'],
            amount=transaction['amount'],
            currency=transaction['currency'],
            email=transaction['email'],
            client_link=transaction['client_link'],
            desc=transaction['desc'],
            date=str(transaction['date'])
        ),
        reply_markup=kb_transaction_tax_back
    )

