from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from app.handlers.commands import start_command
from app.keyboards.inline import inline_back_to_main_menu
from app.utils.callback_data import MainMenuCallbackData, MainMenuAction, BackToMainMenuCallbackData

router = Router()


@router.callback_query(MainMenuCallbackData.filter(F.action == MainMenuAction.ABOUT))
async def about_message(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        f"Loyiha maqsadi — foydalanuvchilarga avvaldan belgilangan mezonlar asosida avtomobillarni sotish bo‘yicha yangi e’lonlarni kuzatib borish imkoniyatini beruvchi Telegram-bot yaratish. Bot qulay, samarali va monitoring jarayonini boshqarish uchun qulay funksiyalarni taqdim etishi kerak.",
        reply_markup=inline_back_to_main_menu())


@router.callback_query(BackToMainMenuCallbackData.filter())
async def back_to_main_menu_message(callback_query: types.CallbackQuery, state: FSMContext):
    await start_command(callback_query.message, state)
