import loggingfrom aiogram import Botimport configasync def on_startup_notify(bot: Bot):    for admin in config.ADMINS:        try:            await bot.send_message(admin, "Bot ishga tushdi")        except Exception as err:            logging.exception(err)