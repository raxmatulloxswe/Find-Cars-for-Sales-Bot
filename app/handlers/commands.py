from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from app.keyboards.inline import inline_main_menu, inline_choose_language
from app.utils.states import RegistrationStateGroup

router = Router()


@router.message(Command('start'))
async def start_command(message: types.Message, state: FSMContext):
    await message.answer("Tilni Tanlang | Choose lang | выберите язык", reply_markup=inline_choose_language())
    await state.set_state(RegistrationStateGroup.language)

@router.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer("Available commands:\n/start - Start the bot\n/help - Get help")
