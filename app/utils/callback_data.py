from enum import Enum
from aiogram.filters.callback_data import CallbackData


# language
class ChooseLanguageAction(str, Enum):
    ENG = 'en'
    UZB = 'uz'
    RUS = 'ru'


class ChooseLanguageCallbackData(CallbackData, prefix='choose_lang'):
    language: ChooseLanguageAction


def cb_choose_language_callback_data(lang):
    return ChooseLanguageCallbackData(language=lang.value).pack()


# main menu
class MainMenuAction(str, Enum):
    NEW_DETECT = 'new_detect'
    ABOUT = 'about'
    MY_ORDERS = 'my_orders'
    HISTORY_DETECT = 'history_detect'
    SETTINGS = 'settings'


class MainMenuCallbackData(CallbackData, prefix='main_menu'):
    action: MainMenuAction


def cb_main_menu_callback_data(action):
    return MainMenuCallbackData(action=action.value).pack()


class Go_To_MenuAction(str, Enum):
    GO = 'go'


class Go_To_MenuCallbackData(CallbackData, prefix='back_main_menu'):
    action: Go_To_MenuAction


def cb_go_to_main_menu_callback_data():
    return Go_To_MenuCallbackData(action=Go_To_MenuAction.GO.value).pack()


# back
class BackToMainMenuAction(str, Enum):
    BACK = 'back'


class BackToMainMenuCallbackData(CallbackData, prefix='back_main_menu'):
    action: BackToMainMenuAction


def cb_back_to_main_menu_callback_data():
    return BackToMainMenuCallbackData(action=BackToMainMenuAction.BACK.value).pack()

