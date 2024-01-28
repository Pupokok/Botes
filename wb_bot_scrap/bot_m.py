import os
import logging
import asyncio
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from handlers import admin


load_dotenv()
bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot=bot)

async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(admin.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())