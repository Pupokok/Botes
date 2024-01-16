import os
import logging
import asyncio
from handlers import client
from dotenv import load_dotenv
import aioschedule as schedule
from aiogram import Dispatcher, Bot
from functions.main import main_card_parse, sec_card_parse

load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot=bot)

async def main():
    dp.include_routers(client.router)
    await bot.delete_webhook(drop_pending_updates=True)
    scheduler_task = asyncio.create_task(scheduler())  
    await dp.start_polling(bot)
    await scheduler_task  



last_main_article_data = None
last_sec_articles = []

async def check_and_send_updates():
    global last_main_article_data, last_sec_articles

    main_article_data = main_card_parse()
    if main_article_data and main_article_data != last_main_article_data:
        last_main_article_data = main_article_data
        main_article_text = "\n".join(main_article_data)
        await bot.send_message(chat_id=os.getenv('CHAT_ID'), text=main_article_text)

    sec_articles = sec_card_parse()
    for article_data in sec_articles:
        if article_data['title'] not in [article['title'] for article in last_sec_articles]:
            last_sec_articles.append(article_data)
            article_text = "\n".join([
                f"<b>{article_data['title']}</b>",
                article_data['subtitle'],
                *article_data['text_paragraphs']
            ])
            if article_data['img_url']:
                article_text += f"\n{article_data['img_url']}"
            await bot.send_message(chat_id=os.getenv('CHAT_ID'), text=article_text)
            await asyncio.sleep(10)

async def scheduler():
    schedule.every(1).minutes.do(check_and_send_updates)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())