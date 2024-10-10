from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import L, I18nContext

from domain.states.admin.message.MessagingState import MessagingState
from domain.states.admin.message.NotificationTools import NotificationTools
from presentation.keyboards.admin.kb_messaging.kb_messaging import kb_media_skip, SkipMediaMessaging, kb_media_send, \
    SendMessageMessaging

router = Router()


@router.message(MessagingState.Message)
async def set_message(message: Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(message=message.html_text)
    await state.set_state(MessagingState.Image)
    await message.answer(i18n.MESSAGING.INPUT.IMAGE(), reply_markup=kb_media_skip)


@router.message(MessagingState.Image, F.photo)
async def set_image(message: Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await message.answer_photo(photo=data['photo'], caption=data['message'], reply_markup=kb_media_send)


@router.callback_query(SkipMediaMessaging.filter())
async def media_skip(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    await callback.message.answer(data['message'], reply_markup=kb_media_send)


@router.callback_query(SendMessageMessaging.filter())
async def send_message(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()

    result = await NotificationTools.push_all_clients(data, bot, i18n)

    await callback.message.answer(result)
