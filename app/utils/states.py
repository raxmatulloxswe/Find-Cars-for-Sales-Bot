from aiogram.fsm.state import StatesGroup, Stateclass RegistrationStateGroup(StatesGroup):    language = State()    phone = State()    name = State()    finish = State()class DetectStateGroup(StatesGroup):    main_menu = State()    model_name = State()