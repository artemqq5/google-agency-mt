import asyncio
import os

import pandas as pd
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, Document
from aiogram_i18n import I18nContext

from data.repositories.taxes import TaxRepository
from data.repositories.transaction_rep.tax_transaction import TaxTransactionRepository
from domain.states.admin.TaxPaymentState import TaxPaymentState
from presentation.keyboards.admin.kb_specific.kb_specific import SpecificLoadTaxPayment

router = Router()


@router.callback_query(SpecificLoadTaxPayment.filter())
async def load_taxpayment(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(TaxPaymentState.File)
    await callback.message.answer(i18n.ADMIN.SPECIFIC.TAX.DOCUMENT())


@router.message(TaxPaymentState.File, F.document and F.document.mime_type == "text/csv")
async def taxpayment_docs(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    await state.set_state(None)

    document: Document = message.document
    file_path = f"temp_{document.file_name}"
    # Завантаження файлу
    file = await bot.download(document.file_id)
    try:
        # Зчитування CSV файлу
        with open(file_path, "wb") as f:
            f.write(file.read())

        data_dict = pd.read_csv(file_path).to_dict(orient='records')  # Перетворення в масив словників
        for data in data_dict:
            result = TaxTransactionRepository().add_tax_transaction(data)
            if result['result']:
                tax_data = TaxRepository().get(result['taxID'])
                await message.answer(i18n.ADMIN.SPECIFIC.TAX.SUCCESS(
                    id=tax_data['transaction_uuid'], client_link=tax_data['client_link'],
                    kind=tax_data['kind'], team=tax_data['team_name'], amount=tax_data['amount'],
                    currency=tax_data['currency'], status=tax_data['status'], email=tax_data['email'],
                    desc=tax_data['desc'], date=str(tax_data['date'])
                ))
            else:
                await message.answer(i18n.ADMIN.SPECIFIC.TAX.FAIL(email=data['Google email'], error=result['error']))

    except Exception as e:
        print(e)
        await message.answer(i18n.ADMIN.SPECIFIC.TAX.ERROR(error=str(e)))
    finally:
        os.remove(file_path)


@router.message(TaxPaymentState.File)
async def taxpayment_docs_error(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    await message.answer(i18n.ADMIN.SPECIFIC.TAX.NO_DOCUMENT())
