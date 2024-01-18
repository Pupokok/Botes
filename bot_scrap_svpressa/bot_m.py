import os
import logging
import asyncio
from dotenv import load_dotenv
import aioschedule as schedule
from aiogram import Dispatcher, Bot
from main import main_card_parse, sec_card_parse
from aiogram.filters import CommandStart
from aiogram.types import Message


load_dotenv()
bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot=bot)

async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    scheduler_task = asyncio.create_task(scheduler())  
    await dp.start_polling(bot)
    await scheduler_task


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(text="Привет, я бот по статьям")

async def check_and_send_updates():
    main_articles_data = main_card_parse()

    for main_article_data in main_articles_data:
        title = main_article_data["title"]
        subtitle = main_article_data["subtitle"]
        text_paragraph = "\n".join(main_article_data["text_paragraphs"])
        img_url = main_article_data["img_url"]
        main_article_text = f"{title}\n{subtitle}\n{text_paragraph}\n{img_url}"
        await bot.send_message(chat_id=os.getenv('CHAT_ID'), text=main_article_text)
        await asyncio.sleep(2)

    sec_articles_data = sec_card_parse()

    for article_data in sec_articles_data:
        title = article_data["title"]
        subtitle = article_data["subtitle"]
        text_paragraphs = "\n".join(article_data["text_paragraphs"])
        img_url = article_data["img_url"]
        article_text = f"{title}\n{subtitle}\n{text_paragraphs}\n{img_url}"
        await bot.send_message(chat_id=os.getenv('CHAT_ID'), text=article_text)
        await asyncio.sleep(2)



async def scheduler():
    schedule.every(5).minutes.do(check_and_send_updates)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())