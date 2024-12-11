from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from app.keyboards.inline import inline_main_menu, inline_back_to_main_menu
from app.keyboards.reply import reply_send_phone_number, reply_send_name
from app.utils.states import RegistrationStateGroup
from app.utils.callback_data import ChooseLanguageCallbackData
from app.utils.db_manager import db

router = Router()


@router.callback_query(ChooseLanguageCallbackData.filter())
async def first_handler(callback_query: types.CallbackQuery, state: FSMContext, callback_data: ChooseLanguageCallbackData):
    # Get the user's telegram_id
    telegram_id = callback_query.from_user.id

    # Check if the user exists in the database
    user_exists = await db.get_user_telegram_id(telegram_id)  # Make sure this method exists in your db_manager

    if user_exists:
        # User exists, skip registration and send the main menu
        await callback_query.message.answer("Siz allaqachon ro'yxatdan o'tgan ekansiz", reply_markup=inline_main_menu())
        # await state.set_state(RegistrationStateGroup.main_menu)  # Set the state for main menu
    else:
        # User doesn't exist, proceed with the registration process
        await state.update_data({"language": callback_data.language})

        await callback_query.message.answer(f"Telefon raqamingizni jo`nating", reply_markup=reply_send_phone_number())

        await state.set_state(RegistrationStateGroup.phone)


@router.message(F.text, RegistrationStateGroup.phone)
async def receive_phone(message: types.Message, state: FSMContext):
    if not message.text.startswith('+998') or len(message.text) != 13:
        return message.answer("To`g`ri formatda raqam jo`nating yoki buttondan foydalaning")

    await state.update_data({"phone_number": message.text})
    await state.set_state(RegistrationStateGroup.name)
    await message.answer("Ismingizni jo`nating", reply_markup=types.ReplyKeyboardRemove())


@router.message(F.contact, RegistrationStateGroup.phone)
async def receive_contact(message: types.Message, state: FSMContext):
    user_first_name = message.from_user.first_name

    await state.update_data({"phone_number": f"{message.contact.phone_number}"})
    await state.set_state(RegistrationStateGroup.name)
    await message.answer(
        text="Ismingizni jo`nating yoki tugmachani bosing!",
        reply_markup=reply_send_name(user_first_name)
    )
    # await message.answer("Ismingizni jo`nating", reply_markup=types.ReplyKeyboardRemove())


@router.message(F.text, RegistrationStateGroup.name)
async def receive_name(message: types.Message, state: FSMContext):
    await state.update_data({"name": message.text})
    registration_data = await state.get_data()

    await message.answer(f"Sizning ismingiz: {registration_data['name']}\n"
                         f"Telefon raqamingiz: {registration_data['phone_number']}\n"
                         f"Tiliz: {registration_data['language']}\n\n")
    await message.answer("Asosiy menuga o`tish uchun tugmani bosing!", reply_markup=inline_main_menu())
    await db.create_user(message.from_user.id, registration_data['language'], registration_data['phone_number'],
                         registration_data['name'], message.from_user.username)

    await state.clear()
