from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.utils.callback_data import (cb_choose_language_callback_data, cb_main_menu_callback_data, ChooseLanguageAction,
        MainMenuAction, cb_back_to_main_menu_callback_data, cb_go_to_main_menu_callback_data, Go_To_MenuAction)


def inline_back_to_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Asosiy menu',
                           callback_data=cb_back_to_main_menu_callback_data())
    return inline_keyboard.as_markup()


def inline_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Yangi Qidiruv 🔎',
                           callback_data=cb_main_menu_callback_data(action=MainMenuAction.NEW_DETECT))
    inline_keyboard.add()
    inline_keyboard.button(text='Qidiruv tarixi 📂 ', callback_data=cb_main_menu_callback_data(action=MainMenuAction.HISTORY_DETECT))
    inline_keyboard.button(text='Sozlamalar ⚙️ ️', callback_data=cb_main_menu_callback_data(action=MainMenuAction.SETTINGS))
    # inline_keyboard.button(text='Biz haqimizda ℹ️ ℹ ️', callback_data=cb_main_menu_callback_data(action=MainMenuAction.ABOUT))

    inline_keyboard.adjust(1, 2)

    return inline_keyboard.as_markup()


def inline_choose_language():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='🇺🇿uz', callback_data=cb_choose_language_callback_data(lang=ChooseLanguageAction.UZB))
    inline_keyboard.button(text='🇬🇧 en', callback_data=cb_choose_language_callback_data(lang=ChooseLanguageAction.ENG))
    inline_keyboard.button(text='🇷🇺 ru', callback_data=cb_choose_language_callback_data(lang=ChooseLanguageAction.RUS))

    return inline_keyboard.as_markup()


def inline_subscribe():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Subscribe', url='https://t.me/+GRx6sKGZLn83YWEy')

    return inline_keyboard.as_markup()
