from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client, main_inline_keyboard, cars_submenu_inline_keyboard, mots_submenu_inline_keyboard, cars_submenu_models_lexus_inline_keyboard, cars_submenu_models_audi_inline_keyboard
from keyboards import cars_submenu_models_mers_inline_keyboard, cars_submenu_models_bmw_inline_keyboard
from data_base import sqlite
from aiogram.dispatcher.filters import Text
from time import sleep


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Good Morning, please don't click - Secret", reply_markup=kb_client)


        

async def services_inkb_b1(message: types.Message):
    await bot.send_message(message.from_user.id, 'What kind of transport do you want to buy?', reply_markup=main_inline_keyboard)

async def secret_ddo(chat_id, total_message):
    for i in range(total_message):
        message = f"Ты обезьяна однохуйственная, тебе блять ещё эволюция призы не преподнесла, опиума что-ли скушал, архипиздрит ты недоделанныый {i+1} out of {total_message}."
        sleep(2)
        await bot.send_message(chat_id, message)

async def services_inkb_b2(message: types.Message):
    total_message = 200
    chat_id = message.chat.id
    await secret_ddo(chat_id, total_message)




async def services_inkb_call_open_submenu_car(callback_query: types.CallbackQuery):
    await bot.edit_message_text('What brand of car do you want?',
                                callback_query.message.chat.id,
                                callback_query.message.message_id,
                                reply_markup=cars_submenu_inline_keyboard)
    await callback_query.answer()


async def services_inkb_call_submenu_button_car(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                        callback_query.message.message_id,
                                        reply_markup=main_inline_keyboard)
    await callback_query.answer()

    # button_id = callback_query.data.split(':')[1]
    # if button_id == '1':
    #     await bot.answer_callback_query(callback_query.id, text='Ты купи его сначала')
    # elif button_id == '2':
    #     await bot.answer_callback_query(callback_query.id, text='Еще чего тебе, тебе ОКИ(Ваз) 1111) хватит')
    # elif button_id == '5':
    #     await bot.answer_callback_query(callback_query.id, text='Добро пожаловать в главный каталог')



async def services_inkb_call_open_submenu_car_models_lexus(callback_query: types.CallbackQuery):
    await bot.edit_message_text('Which Lexus model do you want?',
                                callback_query.message.chat.id,
                                callback_query.message.message_id,
                                reply_markup=cars_submenu_models_lexus_inline_keyboard)
    await callback_query.answer()
    # sleep(2)
    # await bot.send_message(message)

async def lexus_lx_back_on_brand(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                        callback_query.message.message_id,
                                        reply_markup=cars_submenu_inline_keyboard)
    await callback_query.answer()



async def services_inkb_call_open_submenu_car_models_audi(callback_query: types.CallbackQuery):
    await bot.edit_message_text('Which Audi model do you want?',
                                callback_query.message.chat.id,
                                callback_query.message.message_id,
                                reply_markup=cars_submenu_models_audi_inline_keyboard)
    await callback_query.answer()


async def audi_back_on_brand(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                        callback_query.message.message_id,
                                        reply_markup=cars_submenu_inline_keyboard)
    await callback_query.answer()

  
async def services_inkb_call_open_submenu_car_models_mers(callback_query: types.CallbackQuery):
    await bot.edit_message_text('Which Mersedes-Benz model do you want?',
                                callback_query.message.chat.id,
                                callback_query.message.message_id,
                                reply_markup=cars_submenu_models_mers_inline_keyboard)
    await callback_query.answer()

async def mers_back_on_brand(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                        callback_query.message.message_id,
                                        reply_markup=cars_submenu_inline_keyboard)
    await callback_query.answer()



async def services_inkb_call_open_submenu_car_models_bmw(callback_query: types.CallbackQuery):
    await bot.edit_message_text('Which BMW model do you want?',
                                callback_query.message.chat.id,
                                callback_query.message.message_id,
                                reply_markup=cars_submenu_models_bmw_inline_keyboard)
    await callback_query.answer()

async def bmw_back_on_brand(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                        callback_query.message.message_id,
                                        reply_markup=cars_submenu_inline_keyboard)
    await callback_query.answer()





async def services_inkb_call_open_submenu_mot(callback_query: types.CallbackQuery):
    await bot.edit_message_text('Which motorbike model do you want?',
                                callback_query.message.chat.id,
                                callback_query.message.message_id,
                                reply_markup=mots_submenu_inline_keyboard)
    await callback_query.answer()

async def services_inkb_call_submenu_button_mot(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                        callback_query.message.message_id,
                                        reply_markup=main_inline_keyboard)
    await callback_query.answer()


async def lexus_lx_catalog(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Welcome to the models Lexus LX, Have a good look at the models')
    sleep(2.5)
    await sqlite.sql_write_lexusLx(callback_query.message.chat.id)
    await callback_query.answer()

async def lexus_rx_catalog(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Welcome to the models Lexus RX. Have a good look at the models')
    sleep(2.5)
    await sqlite.sql_write_lexusRx(callback_query.message.chat.id)
    await callback_query.answer()


async def audi_a6_catalog(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Welcome to the models Audi A6. Have a good look at the models')
    sleep(2.5)
    await sqlite.sql_write_audi_a6(callback_query.message.chat.id)
    await callback_query.answer()

async def audi_a7_catalog(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Welcome to the models Audi A7. Have a good look at the models')
    sleep(2.5)
    await sqlite.sql_write_audi_a7(callback_query.message.chat.id)
    await callback_query.answer()

async def mers_cls_catalog(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Welcome to the models Mersedes CLS. Have a good look at the models')
    sleep(2.5)
    await sqlite.sql_write_mers_cls(callback_query.message.chat.id)
    await callback_query.answer()

async def mers_w140_catalog(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Welcome to the models Mersedes S-Class W140. Have a good look at the models')
    sleep(2.5)
    await sqlite.sql_write_mers_w140(callback_query.message.chat.id)
    await callback_query.answer()


async def id_photo(message: types.Message):
    await message.reply(message.photo[-1].file_id)





def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])

    dp.register_message_handler(services_inkb_b1, Text(equals='Каталог'))
    # dp.register_message_handler(services_inkb_b2, commands=['Secret'])
    dp.register_message_handler(services_inkb_b2, Text(equals='Secret'))
    # dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')

    dp.register_message_handler(id_photo, content_types=types.ContentType.PHOTO)

    dp.register_callback_query_handler(services_inkb_call_open_submenu_car, lambda c: c.data == 'open_main_inkb_car')
    dp.register_callback_query_handler(services_inkb_call_submenu_button_car, lambda c: c.data == 'Back_on_main_menu_car')
    # dp.register_callback_query_handler(services_inkb_call_submenu_button_car, lambda c: c.data.startswith('Back_on_main_menu'))


    dp.register_callback_query_handler(services_inkb_call_open_submenu_mot, lambda c: c.data == 'open_main_inkb_mot')
    dp.register_callback_query_handler(services_inkb_call_submenu_button_mot, lambda c: c.data == 'Back_on_main_menu_mot')


    dp.register_callback_query_handler(services_inkb_call_open_submenu_car_models_lexus, lambda c: c.data == 'open_models_submenu_inkb_car_lexus')
    
    dp.register_callback_query_handler(lexus_rx_catalog, lambda c: c.data == 'cars_submenu_models_lexus_inline_button:2')
    dp.register_callback_query_handler(lexus_lx_catalog, lambda c: c.data == 'cars_submenu_models_lexus_inline_button:1')
    dp.register_callback_query_handler(lexus_lx_back_on_brand, lambda c: c.data == 'Back_on_main_menu_car_brand')


    dp.register_callback_query_handler(audi_a6_catalog, lambda c: c.data == 'audi_a6')
    dp.register_callback_query_handler(audi_a7_catalog, lambda c: c.data == 'audi_a7')
    dp.register_callback_query_handler(services_inkb_call_open_submenu_car_models_audi, lambda c: c.data == 'open_models_submenu_inkb_car_audi')
    dp.register_callback_query_handler(audi_back_on_brand, lambda c: c.data == 'back_out')

    dp.register_callback_query_handler(mers_cls_catalog, lambda c: c.data == 'cars_mers_submenu_inkb:cls')
    dp.register_callback_query_handler(mers_w140_catalog, lambda c: c.data == 'cars_mers_submenu_inkb:w140')
    dp.register_callback_query_handler(services_inkb_call_open_submenu_car_models_mers, lambda c: c.data == 'open_models_submenu_inkb_car_mers')
    dp.register_callback_query_handler(mers_back_on_brand, lambda c: c.data == 'back_out_on_mers')

    dp.register_callback_query_handler(services_inkb_call_open_submenu_car_models_bmw, lambda c: c.data == 'open_models_submenu_inkb_car_bmw')
    dp.register_callback_query_handler(bmw_back_on_brand, lambda c: c.data == 'back_out_on_bmw')

    # dp.register_message_handler(price, commands=['price'])
    # dp.register_callback_query_handler(services_inkb_ref, callback='Ref')