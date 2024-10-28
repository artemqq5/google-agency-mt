from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from presentation.keyboards.client.kb_main_client import kb_faq

router = Router()


@router.message(F.text == L.FAQ())
async def faq(message: Message, i18n: I18nContext, state: FSMContext):
    await message.answer(i18n.FAQ_MESSAGE(), reply_markup=kb_faq)
