import os
import re
import asyncio
import time
import pytz

from dotenv import load_dotenv
from datetime import datetime
from aiogram import Router
from aiogram.types import Message, URLInputFile
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from filters.is_admin import IsAdmin
from bot_m import bot
from main import ParseWB
from keyboards.admin_kb import kb_admin
from utils.states import Currency, Times

router = Router()
load_dotenv()
result = None

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text="Привет, я парсер wildberries", reply_markup=kb_admin)

@router.message(lambda message: message.text == "Сменить время", IsAdmin(os.getenv('ID_GROUP')))
async def change_time(message: Message, state: FSMContext):
        await state.set_state(Times.first_var)
        await message.answer("Напишите 1 переменную, идут 2 переменные которые умножаются друг на друга")

@router.message(Times.first_var)
async def firs_vat(message: Message, state: FSMContext):
    first_var = message.text
    if not first_var.isdigit():
        await message.answer("Пожалуйста, введите число для второй переменной.")
        return
    await state.update_data(first_var=first_var)
    await state.set_state(Times.second_var)
    await message.answer("Напишите 2 переменную")

@router.message(Times.second_var)
async def secod_var(message: Message, state: FSMContext):
    global result
    second_var = message.text
    if not second_var.isdigit():
        await message.answer("Пожалуйста, введите число для второй переменной.")
        return
    await state.update_data(second_var=second_var)
    take_time = await state.get_data()
    fir_ti = take_time.get("first_var")
    sec_ti = take_time.get("second_var")
    result = int(fir_ti) * int(sec_ti)
    await state.clear()


@router.message(lambda message: message.text == "Добавить товар", IsAdmin(os.getenv('ID_GROUP')))
async def curency_add(message: Message, state: FSMContext):
    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz)
    start_hour = 7
    end_hour = 22
    if start_hour <= current_time.hour < end_hour:
        await state.set_state(Currency.url)
        await message.answer("Отправьте ссылку")
    else:
        await message.reply("Я работаю только с 7 до 10 утра. Пожалуйста, пишите в это время.")

@router.message(Currency.url)
async def hand_cur(message: Message, state: FSMContext):
    list_url = []
    list_item = []
    await state.update_data(url=message.text)
    take_url = await state.get_data()
    add_url = take_url.get("url")
    urls = re.findall(r'https?://[^\s]+', add_url.replace('http://', ' http://').replace('https://', ' https://'))
    
    if urls:
        for url in urls:
            parse_wb = ParseWB(url)
            res = parse_wb.get_seller_id(url)

            list_url.append(url)
            list_item.append({
                'id': res['id'],
                'name': res['name'],
                'rating': res['rating'],
                'price': res['price'],
                'photo': res['photo']
            })
            await asyncio.sleep(2)

        formatted_message = ""
        if list_item:
            for index, item in enumerate(list_item, start=1):
                formatted_message = f"{item['name']}\n\nАртикул <a href='{list_url[index-1]}'>{item['id']}</a>\n\n⭐️{item['rating']}\nЦена:<b>{item['price']}</b>₽"
                image = URLInputFile(
                    item['photo'],
                    filename="python-logo.png"
                )
                await bot.send_photo(chat_id=os.getenv('CHAT_ID'), photo=image, caption=formatted_message)
                # if len(times_list) >= 1:
                time.sleep(result)                
    else:
        await message.answer("Не найдено ни одной ссылки")
    await state.clear()