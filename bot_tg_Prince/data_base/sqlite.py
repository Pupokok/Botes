import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('car.db')
    cur = base.cursor()
    if base:
        print('Data base connected')
    base.execute('CREATE TABLE IF NOT EXISTS menu(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, img BLOB, name TEXT, description TEXT, price TEXT, brand TEXT, model TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu (img, name, description, price, brand, model) VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_write_lexusLx(callback_query):
    for ret in cur.execute("SELECT img, name, description, price FROM menu WHERE ID IN (?) ", [1]):
        await bot.send_photo(callback_query, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nЦеновая категория от {ret[3]}')

async def sql_write_lexusRx(callback_query):
    for ret in cur.execute("SELECT img, name, description, price FROM menu WHERE ID IN (?, ?) ", [2, 3]):
        await bot.send_photo(callback_query, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nЦеновая категория от {ret[3]}')
    
async def sql_write_audi_a6(callback_query):
    for ret in cur.execute("SELECT img, name, description, price FROM menu WHERE ID IN (?) ", [4]):
        await bot.send_photo(callback_query, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nЦеновая категория от {ret[3]}')

async def sql_write_audi_a7(callback_query):
    for ret in cur.execute("SELECT img, name, description, price FROM menu WHERE ID IN (?) ", [5]):
        await bot.send_photo(callback_query, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nЦеновая категория от {ret[3]}')

async def sql_write_mers_cls(callback_query):
    for ret in cur.execute("SELECT img, name, description, price FROM menu WHERE ID IN (?) ", [6]):
        await bot.send_photo(callback_query, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nЦеновая категория от {ret[3]}')

async def sql_write_mers_w140(callback_query1):
    for ret1 in cur.execute("SELECT img, name, description, price FROM menu WHERE ID IN (?) ", [7]):
        await bot.send_photo(callback_query1, ret1[0], f'{ret1[1]}\n\n{ret1[2]}\n\nЦеновая категория от {ret1[3]}')