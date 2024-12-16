from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.utils.callback_data import (cb_choose_language_callback_data, cb_main_menu_callback_data, ChooseLanguageAction,
        MainMenuAction, cb_back_to_main_menu_callback_data, DetectModelAction, cb_detect_model_callback_data,
    DetectModelNameAction, cb_detect_model_name_callback_data, DetectModelNameKIAAction, cb_detect_model_name_KIA_callback_data,
    cb_detect_model_name_jetour_callback_data, DetectModelNameJetourAction, cb_detect_model_name_byd_callback_data, DetectModelNameBYDAction)


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


def inline_new_detect():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Chevrolet', callback_data=cb_detect_model_callback_data(action=DetectModelAction.CHEVROLET))
    inline_keyboard.button(text='Jetour', callback_data=cb_detect_model_callback_data(action=DetectModelAction.JETOUR))
    inline_keyboard.button(text='BYD', callback_data=cb_detect_model_callback_data(action=DetectModelAction.BYD))
    inline_keyboard.button(text='KIA', callback_data=cb_detect_model_callback_data(action=DetectModelAction.KIA))
    inline_keyboard.button(text='Hyundai', callback_data=cb_detect_model_callback_data(action=DetectModelAction.HYUNDAI))
    inline_keyboard.button(text='Mercedes-Benz', callback_data=cb_detect_model_callback_data(action=DetectModelAction.MERCEDES_BENZ))

    inline_keyboard.adjust(2)
    return inline_keyboard.as_markup()


def inline_new_detect_model_chevrolet():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Nexia', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.NEXIA))
    inline_keyboard.button(text='Nexia 3', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.NEXIA_3))
    inline_keyboard.button(text='Spark', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.SPARK))
    inline_keyboard.button(text='Labo', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.LABO))
    inline_keyboard.button(text='Damas', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.DAMAS))
    inline_keyboard.button(text='Cobalt', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.COBALT))
    inline_keyboard.button(text='Gentra', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.GENTRA))
    inline_keyboard.button(text='Onix', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.ONIX))
    inline_keyboard.button(text='Tracker', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.TRACKER))
    inline_keyboard.button(text='Captiva', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.CAPTIVA))
    inline_keyboard.button(text='Malibu', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.MALIBU))
    inline_keyboard.button(text='Eqinox', callback_data=cb_detect_model_name_callback_data(action=DetectModelNameAction.EQUINOX))

    inline_keyboard.adjust(2)
    return inline_keyboard.as_markup()


def inline_new_detect_name_model_jetour():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='X70 plus', callback_data=cb_detect_model_name_jetour_callback_data(action=DetectModelNameJetourAction.X70_PLUS))
    inline_keyboard.button(text='X90 plus', callback_data=cb_detect_model_name_jetour_callback_data(action=DetectModelNameJetourAction.X90_PLUS))
    inline_keyboard.button(text='X95 plus', callback_data=cb_detect_model_name_jetour_callback_data(action=DetectModelNameJetourAction.X95_PLUS))
    inline_keyboard.button(text='dashing', callback_data=cb_detect_model_name_jetour_callback_data(action=DetectModelNameJetourAction.DASHING))

    inline_keyboard.adjust(2)
    return inline_keyboard.as_markup()


def inline_new_detect_name_model_byd():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Chazor', callback_data=cb_detect_model_name_byd_callback_data(action=DetectModelNameBYDAction.CHAZOR))
    inline_keyboard.button(text='Yuan', callback_data=cb_detect_model_name_byd_callback_data(action=DetectModelNameBYDAction.YUAN))
    inline_keyboard.button(text='BYD Song Plus', callback_data=cb_detect_model_name_byd_callback_data(action=DetectModelNameBYDAction.SONG_PLUS))
    inline_keyboard.button(text='BYD HAN', callback_data=cb_detect_model_name_byd_callback_data(action=DetectModelNameBYDAction.HAN))
    inline_keyboard.button(text='BYD E2', callback_data=cb_detect_model_name_byd_callback_data(action=DetectModelNameBYDAction.E2))

    inline_keyboard.adjust(2)
    return inline_keyboard.as_markup()


def inline_new_detect_name_model_kia():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Sonet', callback_data=cb_detect_model_name_KIA_callback_data(action=DetectModelNameKIAAction.SONET))
    inline_keyboard.button(text='Seltos', callback_data=cb_detect_model_name_KIA_callback_data(action=DetectModelNameKIAAction.SELTOS))
    inline_keyboard.button(text='KIA K5', callback_data=cb_detect_model_name_KIA_callback_data(action=DetectModelNameKIAAction.K5))
    inline_keyboard.button(text='Carnival', callback_data=cb_detect_model_name_KIA_callback_data(action=DetectModelNameKIAAction.CARNIVAL))
    inline_keyboard.button(text='Stringer', callback_data=cb_detect_model_name_KIA_callback_data(action=DetectModelNameKIAAction.STRINGER))

    inline_keyboard.adjust(2)
    return inline_keyboard.as_markup()