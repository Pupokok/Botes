import asyncio
import aioschedule as schedule

from aiogram import types

async def scheduler():
    schedule.every().day.at("15:32").do(daily_send_messages)
    schedule.every().day.at("19:00").do(daily_send_messages)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)

async def daily_send_messages(message: types.Message):
    daily_mes = "\n".join([
        "🕹️ ИГРА ЧЕРЕЗ 15 МИНУТ 🕹️",
        "Делаем ставки согласно инструкции ниже:",
        "🟢1 ставка - авто вывод (коэф 1.30 страховка)",
        "Пример ставки - 1 000₽",
        "🔴2 ставка - риск (коэф от 1.70 и выше)", 
        "Пример ставки - 300₽",
        "По этому сигналу ставим на раунд:",
        "🚀СТАВИМ",
        "⚠️НЕ ЗАБУДЬТЕ ПЕРЕД ИГРОЙ ВЫКЛЮЧИТЬ VPN ДЛЯ КОРРЕКТНОЙ РАБОТЫ САЙТА",
        "Ссылка на игру - https://1wyodo.top/",
        "❗️Не забываем пополнить банк перед игрой."
    ])
    await message.bot.send_message(chat_id=1037988700, text=daily_mes)
