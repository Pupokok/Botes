#                                                                                                                                        #                                  
#                                     ░█████╗░██╗░░░░░░█████╗░░█████╗░████████╗██████╗░░█████╗░███████                                   #
#                                     ██╔══██╗██║░░░░░██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚════██                                   #
#                                     ███████║██║░░░░░██║░░╚═╝███████║░░░██║░░░██████╔╝███████║░░███╔═                                   #
#                                     ██╔══██║██║░░░░░██║░░██╗██╔══██║░░░██║░░░██╔══██╗██╔══██║██╔══╝░                                   #
#                                     ██║░░██║███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║███████                                   #
#                                     ╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════                                   #

import os
import json
import string
import sqlite3 as sq
from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

answ = dict()
ID = None
load_dotenv()

storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def on_startup(_):
    print('Skull on the phone')
    sql_start()

# Получаем ID текущего модератора
@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def change_moderator(message: types.Message):
    global ID 
    ID = message.from_user.id
    await bot.send_message(message.from_user.id,
                           'Master, what do you want from me?',
                           reply_markup=button_case_admin)
    await message.delete()

# Начало диалога загрузки нового пункта меню
@dp.message_handler(commands=['Load'], state=None)
async def load_start(message: types.Message):
    if message.from_user.id ==ID:
        await FSMAdmin.photo.set()
        await message.reply('Load photo')

# Ловим 1 ответ и пишем в словарь
@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state=FSMContext):
        if message.from_user.id ==ID:
            async with state.proxy() as data:
                data['photo'] = message.photo[0].file_id
            await FSMAdmin.next()
            await message.reply('Please enter title')

# Ловим 2 ответ
@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
        if message.from_user.id ==ID:
            async with state.proxy() as data:
                data['name'] = message.text
            await FSMAdmin.next()
            await message.reply('Please enter description')

# Ловим 3 ответ
@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
       if message.from_user.id ==ID:
            async with state.proxy() as data:
                data['description'] = message.text
            await FSMAdmin.next()
            await message.reply('Please enter price')

# Ловим 4 ответ and используем полученные данные 
@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id ==ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await sql_add_command(state)
        await state.finish()

# Выход из состояний
@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id ==ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Ok')

button_load = KeyboardButton('/Load')
button_delete = KeyboardButton('/Delete')
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
            .add(button_delete)

# Inlain buttons
urlkb = InlineKeyboardMarkup(row_width=3)
urlButton1 = InlineKeyboardButton(text='1 VK', 
                                  url='https://vk.com')
urlButton2 = InlineKeyboardButton(text='2 Behance',
                                  url='https://www.behance.net/galleries')
urlkb.add(urlButton1)
x = [InlineKeyboardButton(text='3 OK',
                          url='https://vk.com/alcatraz2241'),
    InlineKeyboardButton(text='4 Ислям',
                         url='https://vk.com/kriskic'),\
    InlineKeyboardButton(text='5 Макс',
                         url='https://vk.com/kaldun228')]
urlkb.row(urlButton2).row(*x).add(InlineKeyboardButton(text='Комрон', url='https://vk.com/id662202676')).insert\
    (InlineKeyboardButton(text='Audio', url='https://vk.com/audio138758209_456241445_5404069352a8a1efd0')).insert

# CallBack button
cbkb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Yes', callback_data='Like_1'),\
                                            InlineKeyboardButton(text='No', callback_data='Like_-1'))
# cbkb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Please enter', callback_data='На глаз себе нажми придурок'))

@dp.message_handler(commands='Test')
async def test_com(message: types.Message):
    await message.answer('Ислям еблан', reply_markup=cbkb)

@dp.callback_query_handler(Text(startswith='Like'))
async def call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('')
    else:
        await callback.answer('Спасибо за голос', show_alert=True)
#    await callback.answer('Спасибо за голос', show_alert=True)
   
    # await callback.answer('Ты Еблан?',show_alert=True)
    # await callback.message.answer('На глаз себе нажми придурок')

# @dp.message_handler(commands='eye')
# async def test_com(message: types.Message):
#     await message.answer('Нажми ты же хочешь', reply_markup=cbkb)

# @dp.callback_query_handler(text='На глаз себе нажми придурок')
# async def call(callback: types.CallbackQuery):
#     await callback.message.answer('На глаз себе нажми придурок')
#     await callback.answer('Ты Еблан?',show_alert=True)

# Команда старта и кнопки
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    k1 = KeyboardButton('Режим работы')
    k2 = KeyboardButton('Расположение')
    k3 = KeyboardButton('Услуги')
    k4 = KeyboardButton('Меню')
    kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_client.insert(k1)
    kb_client.add(k2)
    kb_client.insert(k3)
    kb_client.insert(k4)
    
    try:
        await bot.send_message(message.from_user.id,
                               'Vas приветствует компания LOK',
                               reply_markup=kb_client)
    except:
        await message.reply('Please write to the bot')

#Command режим работы
@dp.message_handler(text=['Режим работы'])
async def command_power(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Круглосуточно',
                           reply_markup=None)

#Command Услуги
@dp.message_handler(text=['Услуги'])
async def command_user(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Создание лендинга',
                           reply_markup=None)

#Command Расположение
@dp.message_handler(text=['Расположение'])
async def command_rasp(message: types.Message):
    await bot.send_message(message.from_user.id,
                           '55°47,45 c. ш. 49°6,87 в. д',
                           reply_markup=None)
#Command Menu
@dp.message_handler(text=['Меню'])
async def menu(message: types.Message):
    await sql_read(message)

@dp.message_handler(lambda message: ('уебан') in message.text.lower())
async def ueban(message: types.Message):
    await bot.send_message(message.from_user.id, 
                           'Ты обезьяна однохуйственная,'
                           'тебе блять ещё эволюция призы не преподнесла,'
                           'опиума что-ли скушал,'
                           'архипиздрит ты недоделанныый')
    await message.delete()

@dp.message_handler(lambda message: 'хуй' in message.text)
async def hui(message: types.Message):
    await bot.send_message(message.from_user.id, "помолчи хуета, сиди в обиде ребёнок мертвой шалавы Заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии.пиздобратия мандопроушечная, уебище залупоглазое, дрочепиздище хуеголовое, пробиздоблядская мандопроушина, гнидопаскудная хуемандовина, ах ты блядь семитаборная чтоб тебя всем столыпином харили, охуевшее блядепиздопроёбище чтоб ты хуем поперхнулся долбоебическая пиздорвань, хуй тебе в глотку через анальный проход, распизди тебя тройным перебором через вторичный переёб пиздоблятское хуепиздрическое мудовафлоебище сосущее километры трипперных членов, трихломидозопиздоеблохуе блядеперепиздическая спермоблевотина, гандон с гонореей... Да разъебись ты троебучим проебом сперматоблятская пиздапроебина охуевающая в своей пидарастической сущности похожаю на ебущегося в жопу енота, сортирующего яйца в пизде кастрированной кобылы. Хуелептический пиздопрозоид, еблоухий мандохвост. Ебун хуеголовый, пидрасня ебаная. Залупоголовая блядоящерица. Трипиздоблядская промудохуина! Распроеб твою в крестище через коромысло в копейку мать! Что за блядская пиздопроебина, охуевающая своей пидорестической заебучестью невъебенной степени охуения. Заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии. Мордоблядина залупоглазая. Ебись ты триебучим проебом пиздуй пока трамваи ходят. Склипездень двужопостворчатый. Злоебучее страхопиздище трипиздоблятский мандопроеб найвыебенищее распиздоблятство! Застрявший в ебенгво гавнопрягопизд отпизднутый от хуеблища и ебанагандонный хуепедераст. Мудагавнопердь. Стоебучее страхопиздище охуевающее в собственной пидарастической злоебучести... Cемиголовый восьмихуй с четырьмя пиздопроебинами. Облямудевшая страпиздихуюлина. Пидористический мудаблядин. Трипездоклятый мудопроеб. Промудохуеблядская пиздопроебина, невьебенно охуевающая от своей собственной облядипизденелости. Трипиздоблядское мудопроебное трипиздие, ебоблядище охуевающее от собственной злоебучести. Облямуденный злоебучий страхопизднутый трихуемандаблядский ебаквакнутый распиздаеб... Да разъебись ты триебучим проебом хуепуполо залупоглазое, промонодблядская трипиздыпроебина. Хуеблядская пиздопроебина. Да разъебись ты тризлоебучим пробиздом тримандаблядская пиздопроушина охуевающая от собственного блядского невъебения! Шлюшья мразота приохуебенивающая от собственного недохуеплетского злоетрахания. Да произпездуй с 2000 этажа своей припиздоблядской тушей на землю в труху! Трипиздоблядское мудопроебное трипиздие, ебоблядище охуевающее от собственной злоебучести. Облямуденный злоебучий страхопизднутый трихуемандаблядский ебаквакнутый распиздаеб... Хуесосляблядивый расхуйдяй припиздоблядского четвертоногого происхождения прошу завали свой хуеобрыганский блядозвукоговоритель. Промудохуепиздамразоблядское злоепиздие, ебоблядищая пиздопроебина сама ахуевающее от того какая оно пездоблядехуепроклятое. Обосробосанная пиздоблядмна двадцати головая семихуюлина припиздовывающее от хуеглотности своей трипиздговноглоталки. Облямудевшая хуеблядина четырестохуйная и двестипёздная мразотоблядская шлюхасосалка. Хуесосная мудохуепиздопроебная мудаблядина сукв безмаманя блядь шмара козельуебок сдохни хуесоска ебланафт чмырь пидорска манда тупая гандопляс пидрила ебалай долбоеб обмудок овцееб дауниха ненавижу гомодрилла сучка шлюха трахарила гавносос миньетчик пидэраст пиздоеб хуеплет кончиглот ебище сын шлюхи гавноеб мудяра еботрон вафлеглот ебалдуй захуятор имбицил подонок пиздопромудище выебок ахуяэетер ебозер пиздолиз злоуебок хуиман ебил долбоебина пиндос мудазвон хуеб амеба хуйло хуила пиздорвань смесь ебланства и говна ебанат умалишенный дегенерат мандопроушина очкоблут")
    await message.delete()

# Inline buttons
@dp.message_handler(commands='Ref')
async def url_command(message: types.Message):
    await message.answer('Ссылки', reply_markup=urlkb)

#Хэндлер для матов and NO COMMANDS
@dp.message_handler()
async def mat(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
        .intersection(set(json.load(open('mat.json')))) != set():
        await message.answer('Маты запрещены, предупреждение №1')
        await message.delete()
    else:
        await bot.send_message(message.from_user.id,
                               'No commands')
        await message.delete()


#Base of SQL
def sql_start():
    global base, cur
    base = sq.connect('Web_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

#Словарь
async def  sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
     for ret in cur.execute('SELECT * FROM menu').fetchall():
         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nPrice {ret[-1]}')



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)