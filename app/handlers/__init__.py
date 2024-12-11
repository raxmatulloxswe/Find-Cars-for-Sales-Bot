from .commands import router as commands_router
from .about import router as about_router
from .menu import router as menu_router
from .registration import router as registration_router


def setup_handlers(dp):
    dp.include_router(commands_router)
    dp.include_router(menu_router)
    dp.include_router(registration_router)
    dp.include_router(about_router)
