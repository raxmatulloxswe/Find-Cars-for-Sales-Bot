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


class DetectModelAction(str, Enum):
    CHEVROLET = 'chevrolet'
    JETOUR = 'jetour'
    BYD = 'byd'
    KIA = 'kia'
    HYUNDAI = 'hyundai'
    MERCEDES_BENZ = 'mercedes_benz'


class DetectModelCallbackData(CallbackData, prefix='detect_model'):
    action: DetectModelAction


def cb_detect_model_callback_data(action):
    return DetectModelCallbackData(action=action.value).pack()


class DetectModelNameAction(str, Enum):
    NEXIA = 'nexia'
    NEXIA_3 = 'nexia_3'
    SPARK = 'spark'
    LABO = 'labo'
    COBALT = 'cobalt'
    GENTRA = 'gentra'
    DAMAS = 'damas'
    TRACKER = 'tracker'
    CAPTIVA = 'captiva'
    MALIBU = 'malibu'
    ONIX = 'onix'
    EQUINOX = 'equinox'


class DetectModelNameCallbackData(CallbackData, prefix='detect_model_name'):
    action: DetectModelNameAction


def cb_detect_model_name_callback_data(action):
    return DetectModelNameCallbackData(action=action.value).pack()


class DetectModelNameJetourAction(str, Enum):
    X70_PLUS = 'x70_plus'
    X90_PLUS = 'x90_plus'
    X95_PLUS = 'x95_plus'
    DASHING = 'dashing'



class DetectModelNameJetourCallbackData(CallbackData, prefix='detect_model_name_jetour'):
    action: DetectModelNameJetourAction


def cb_detect_model_name_jetour_callback_data(action):
    return DetectModelNameJetourCallbackData(action=action.value).pack()


class DetectModelNameBYDAction(str, Enum):
    CHAZOR = 'CHAZOR'
    YUAN = 'Yuan'
    SONG_PLUS = 'Song Plus'
    HAN = 'BYD_HAM'
    E2 = 'BYD_E2'


class DetectModelNameBYDCallbackData(CallbackData, prefix='detect_model_name_byd'):
    action: DetectModelNameBYDAction


def cb_detect_model_name_byd_callback_data(action):
    return DetectModelNameBYDCallbackData(action=action.value).pack()


class DetectModelNameKIAAction(str, Enum):
    SONET = 'Sonet'
    SELTOS = 'Seltos'
    K5 = 'k5'
    CARNIVAL = 'Carnival'
    STRINGER = 'Stringer'


class DetectModelNameKIACallbackData(CallbackData, prefix='detect_model_name_kia'):
    action: DetectModelNameKIAAction


def cb_detect_model_name_KIA_callback_data(action):
    return DetectModelNameKIACallbackData(action=action.value).pack()