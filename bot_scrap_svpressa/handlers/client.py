import os
from time import sleep
from dotenv import load_dotenv
from bot_m import bot
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from functions.main import main_card_parse, sec_card_parse

load_dotenv()
router = Router()
last_published_data = None

@router.message(CommandStart())
async def start(message: Message):
    
    main_article_data = main_card_parse()
    if main_article_data:
        main_article_text = f"{main_article_data[0]}\n"
        main_article_text += f"{main_article_data[1]}\n"
        main_article_text += "\n".join(main_article_data[2:4])
        if main_article_data[4]:
            main_article_text += f"{main_article_data[4]}\n"
        await bot.send_message(chat_id=os.getenv('CHAT_ID'), text=main_article_text)

    sec_articles = sec_card_parse()
    for article_data in sec_articles:
        sleep(1) 
        article_text = f"{article_data['title']}\n"
        article_text += f"{article_data['subtitle']}\n"
        article_text += "\n".join(article_data['text_paragraphs'])
        if article_data['img_url']:
            article_text += f"{article_data['img_url']}\n"
        await bot.send_message(chat_id=os.getenv('CHAT_ID'), text=article_text)