from aiogram import types
from keyboards import kb_client
from inline_keyboards import inline_kb
from aiogram.filters import CommandStart, StateFilter
from aiogram import Router
from data_base import sqlite
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import OrderFood


router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'''
Привет 👋
<b>{message.from_user.first_name}</b>

Russellstr_Bot к вашим услугам!

Я бот помощник, подскажу актуальный курс, расскажу о сроках доставки и помогу с оформлением твоего будущего заказа с площадки Poizon🫶

Как я работаю? Ответил ниже 🔽

•Начало работы: /start

•Выход к началу: /menu
    
•Оформить заказ: /buy
''', reply_markup=kb_client)


@router.message(StateFilter(None), lambda message: message.text.lower() in ["/итоговаястоимость", "итоговая стоимость", "итоговаястоимость", "/итоговая стоимость"])
async def cmd_food(message: types.Message, state: FSMContext):
    await state.set_state(OrderFood.choosing_food_name)
    await message.answer(text="Отправьте цену товара в юанях:")

@router.message(OrderFood.choosing_food_name)
async def food_chosen(message: Message, state: FSMContext):
    try:
        chosen_food = int(message.text)
    except ValueError:
        await message.answer("Некорректный ввод. Пожалуйста, введите число.")
        return

    await state.update_data(chosen_food=chosen_food)
    user_data = await state.get_data()
    add_uan = await sqlite.sql_read_cur(message)
    result = user_data['chosen_food'] * add_uan + 750
    result_message = f"Итоговая стоимость равна: {result:.2f}\nДоставка в Россию этого товара выйдет ~1200-1800₽(итоговая цена доставки зависит от размера и модели кроссовок)"
    await message.answer(result_message)
    await state.clear()


@router.message()
async def echo(message: types.Message):
    msg = message.text.lower()

    if msg == "сроки доставки":
        await message.answer("Сроки доставки 15 — 25 дней (В зависимости от региона)")
    elif msg == "актуальный курс":
        act_cur = await sqlite.sql_read_cur(message)
        await message.answer(f"Актуальный курс юаня = {act_cur}")

    elif msg == "товар":
        await sqlite.sql_read(message)
    elif msg == "оформить заказ":
        await message.answer("Для оформления заказа убедитесь что у вас выбран товар", reply_markup=inline_kb)