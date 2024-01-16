from create_bot import bot
from data_base import sqlite
from keyboards import main_admin_kb
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    brand = State()
    model = State()

async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 
                           'Вы в меню модератора, что желаете?',
                           reply_markup=main_admin_kb)

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
          return
    await state.finish()
    await message.reply('Отмена произошла успешно', 
                        reply_markup=main_admin_kb)

async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Please load photo')

async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
                data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Please write name')

async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
                data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Please write description')

async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
                data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Please write price')

async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
                data['price'] = (message.text)
        await FSMAdmin.next()
        await message.reply('Please write brand')
        
async def load_brand(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
                data['brand'] = message.text
        await FSMAdmin.next()
        await message.reply('Please write model')

async def load_model(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
                data['model'] = message.text

        await sqlite.sql_add_command(state)
        await message.reply('Add!!')
        await state.finish()

# async def admin_kb_add(message: types.Message):
#     await bot.send_message(message.from_user.id, 'What do you add', reply_markup=main_admin_kb)

# async def admin_kb_del(message: types.Message):
#     await bot.send_message(message.from_user.id, 'What do you delete')

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(make_changes_command, commands='moderator')
    dp.register_message_handler(cancel_handler, Text(equals='Cancel'), state='*')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(cm_start, Text(equals='Add_product'), state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(load_brand, state=FSMAdmin.brand)
    dp.register_message_handler(load_model, state=FSMAdmin.model)



