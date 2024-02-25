import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Dispatcher, Router, Bot

from func.other import scheduler
from callbacks import navigation
from handlers import client, admin
from data_base.models import async_main
from pay import payment
from middlewares.check_sub import CheckSubscription
from middlewares import other_channel
# from data_base import sqlite

load_dotenv()
router = Router()

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(os.getenv("BOT_TOKEN"), parse_mode="HTML")
    dp = Dispatcher(bot=bot)

    dp.message.middleware(CheckSubscription())

    dp.include_routers(
        client.router,
        navigation.router,
        admin.router,
        payment.router,
        other_channel.chan_r
    )

    await async_main()
    scheduler_task = asyncio.create_task(scheduler())  

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await scheduler_task



if __name__ == "__main__":
    asyncio.run(main())
