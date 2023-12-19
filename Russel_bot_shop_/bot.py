import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import client, admin
from config_reader import config
from data_base import sqlite

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher(bot=bot)
    dp.include_routers(admin.router, client.router, sqlite.router)
    sqlite.sql_start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":

    asyncio.run(main())
