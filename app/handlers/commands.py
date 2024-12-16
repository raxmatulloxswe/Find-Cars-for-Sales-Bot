from aiogram import Router, types, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand

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


@router.message(Command('check_state'))
async def check_state(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    await message.answer(f"State: {current_state}")


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Yordam haqida ma'lumot"),
        BotCommand(command="check_state", description="Qaysi stateda ekanligini ko'rsatadi"),
    ]
    await bot.set_my_commands(commands)