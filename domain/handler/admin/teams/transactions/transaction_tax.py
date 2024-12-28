from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositories.taxes import TaxRepository
from presentation.keyboards.admin.kb_teams.kb_team_transaction import NavigationTeamTransactionTax, \
    TeamTransactionTaxDetail, kb_teams_transaction_tax, kb_transaction_tax_back
from presentation.keyboards.admin.kb_teams.kb_teams import TeamTransactionTax

router = Router()


@router.callback_query(TeamTransactionTax.filter())
async def team_transactions_tax(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    transactions_tax = TaxRepository().taxes_by_team(data['team_uuid'])

    await callback.message.edit_text(
        text=i18n.TEAMS.TRANSACTIONS.TAX(),
        reply_markup=kb_teams_transaction_tax(transactions_tax, data.get('last_page_transaction_tax', 1))
    )


@router.callback_query(NavigationTeamTransactionTax.filter())
async def transactions_tax_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()
    transactions_tax = TaxRepository().taxes_by_team(data['team_uuid'])

    await state.update_data(last_page_transaction_tax=page)

    await callback.message.edit_reply_markup(reply_markup=kb_teams_transaction_tax(transactions_tax, page))


@router.callback_query(TeamTransactionTaxDetail.filter())
async def transaction_tax_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    transaction_uuid = callback.data.split(":")[1]
    transaction = TaxRepository().get(transaction_uuid)

    await callback.message.edit_text(
        text=i18n.TEAMS.TRANSACTIONS.TAX.DETAIL(
            id_transaction=transaction['id'],
            uuid_transaction=transaction['transaction_uuid'],
            team_name=transaction['team_name'],
            mcc_name=transaction['mcc_name'],
            kind=transaction['kind'],
            amount=transaction['amount'],
            currency=transaction['currency'],
            status=transaction['status'],
            email=transaction['email'],
            client_link=transaction['client_link'],
            desc=transaction['desc'],
            date=str(transaction['date'])
        ),
        reply_markup=kb_transaction_tax_back
    )

