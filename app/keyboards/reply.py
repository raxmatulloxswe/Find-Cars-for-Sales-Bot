from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_send_phone_number():
    button = KeyboardButton(text="📞 Send Phone Number", request_contact=True)

    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[[button]],
        resize_keyboard=True,
        one_time_keyboard=True,
        # input_field_placeholder="Please share your phone number:"
    )

    return reply_keyboard


def reply_send_name(user_first_name: str):
    button = KeyboardButton(text=f"{user_first_name}")

    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[[button]],
        resize_keyboard=True,  # Klaviatura o'lchamini moslashtirish
        one_time_keyboard=True,  # Javobdan keyin klaviaturani avtomatik yashirish
        input_field_placeholder="Please share your phone number:"
    )
    return reply_keyboard
