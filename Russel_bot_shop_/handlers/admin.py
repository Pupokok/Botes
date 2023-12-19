from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import Form, Add_sneakers, Currency
from filters.is_admin import IsAdmin
from data_base import sqlite
from keyboards.admin_kb import kb_admin

router = Router()


@router.message(Command("moderator"), IsAdmin([]))
async def moder_check(message: Message):
    await message.answer("Вы в меню модератора, что желаете?", reply_markup=kb_admin)

@router.message(lambda message: message.text in ["Меню товара"], IsAdmin([]))
async def read_moder(message: Message):
    await sqlite.sql_read_admin(message)


@router.message(lambda message: message.text in ["Добавить товар"], IsAdmin([]))
async def start_add(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Отправьте имя:")

@router.message(Form.name)
async def handle_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.price)
    await message.answer("Введите цену:")

@router.message(Form.price)
async def handle_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(Form.descr)
    await message.answer("Введите описание:")

@router.message(Form.descr)
async def form_descr(message: Message, state: FSMContext):
    await state.update_data(descr=message.text)
    await state.set_state(Form.photo)
    await message.answer("Теперь загрузи фото")

@router.message(Form.photo, F.photo)
async def handle_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await sqlite.sql_add_command(photo_file_id, data)
    await message.answer("Товар успешно добавлен в базу данных!")
    await state.clear()


@router.message(lambda message: message.text in ["Изменить товар"], IsAdmin([]))
async def what_id(message: Message, state: FSMContext):
    await state.set_state(Add_sneakers.sneack_id)
    await message.answer("Отправьте ID элемента")

@router.message(Add_sneakers.sneack_id)
async def sneack_id_a(message: Message, state: FSMContext):
    sneack_id = message.text
    if not sneack_id.isdigit():
        await message.answer("Некорректный ввод. Пожалуйста, введите число.")
        return
    await state.update_data(sneack_id=sneack_id)
    await state.set_state(Add_sneakers.sneack_name)
    await message.answer("Отправьте другое имя:")

@router.message(Add_sneakers.sneack_name)
async def sneack_name_a(message: Message, state: FSMContext):
    await state.update_data(sneack_name=message.text)
    await state.set_state(Add_sneakers.sneack_price)
    await message.answer("Отправьте другую цену:")

@router.message(Add_sneakers.sneack_price)
async def sneack_price_a(message: Message, state: FSMContext):
    await state.update_data(sneack_price=message.text)
    await state.set_state(Add_sneakers.sneack_descr)
    await message.answer("Отправьте другое описание:")

@router.message(Add_sneakers.sneack_descr)
async def sneack_descr_a(message: Message, state: FSMContext):
    await state.update_data(sneack_descr=message.text)
    await state.set_state(Add_sneakers.sneack_photo)
    await message.answer("Отправьте другое фото:")

@router.message(Add_sneakers.sneack_photo, F.photo)
async def handle_photo(message: Message, state: FSMContext):
    photo_file_id_up = message.photo[-1].file_id
    sneack_data = await state.get_data()
    sneack_id = sneack_data.get("sneack_id")
    await sqlite.sql_update(photo_file_id_up, sneack_data, sneack_id)
    await message.answer("Товар успешно изменён в базе данных!")
    await state.clear()

@router.message(lambda message: message.text in ["Поменять курс юаней"], IsAdmin([]))
async def curency_add(message: Message, state: FSMContext):
    await state.set_state(Currency.currency_1)
    await message.answer("Отправьте курс юаней:")

@router.message(Currency.currency_1)
async def hand_cur(message: Message, state: FSMContext):
    await state.update_data(curency_1=message.text)
    curency_st = await state.get_data()
    curency = curency_st.get("curency_1")
    await sqlite.sql_update_cur(curency)
    await message.answer(f"Валюта успешно поменена {curency}")
    await state.clear()