import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from app.handlers import setup_handlers
from app.handlers.commands import set_commands
from app.middlewares import setup_middlewares
from app.utils.db_manager import db
from app.utils.notify_admins import on_startup_notify

async def main():
    redis = await Redis.from_url(config.REDIS_URL)

    await db.connect()

    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=RedisStorage(redis=redis))

    setup_middlewares(dp)
    setup_handlers(dp)

    await set_commands(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await on_startup_notify(bot)
    await dp.start_polling(bot)

    await db.disconnect()
