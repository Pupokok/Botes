import sqlite3 as sq
from aiogram.types import Message
from aiogram import Router


router = Router()

def sql_start():
    global base, cur
    base = sq.connect('shop.db')
    cur = base.cursor()
    if base:
        print('Data base connected')
    base.execute('CREATE TABLE IF NOT EXISTS menu(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, photo BLOB, name TEXT, descr TEXT, price TEXT, curency TEXT)')
    base.commit()
    
@router.message()
async def sql_add_command(photo_file_id, data):
    cur.execute('INSERT INTO menu (photo, name, descr, price) VALUES (?, ?, ?, ?)',
            (photo_file_id, data['name'], data['descr'], data['price']))
    base.commit()

@router.message()
async def sql_read(message: Message):
    for ret in cur.execute("SELECT photo, name, descr, price FROM menu"):
        await message.answer_photo(photo=ret[0], caption=f'{ret[1]}\n\n{ret[2]}\n\n{ret[3]}')

@router.message()
async def sql_read_admin(message: Message):
    for ret in cur.execute("SELECT ID, photo, name, descr, price FROM menu").fetchall():
        await message.answer_photo(photo=ret[1], caption=f'ID = {ret[0]}\n\n{ret[2]}\n\n{ret[3]}\n\n{ret[4]}')

@router.message()
async def sql_update(photo_file_id_up, sneack_data, sneack_id):
    cur.execute('UPDATE menu SET name = ?, price = ?, descr = ?, photo = ? WHERE ID = ?', 
                (sneack_data['sneack_name'], sneack_data['sneack_price'], sneack_data['sneack_descr'], photo_file_id_up, sneack_id))
    base.commit()

@router.message()
async def sql_update_cur(curency):
    id_cur = 1
    cur.execute('UPDATE menu SET curency = ? WHERE ID = ?',
                (curency, id_cur))
    base.commit()

@router.message()
async def sql_read_cur(message: Message):
    sneack_ = 1
    cur.execute("SELECT curency FROM menu WHERE ID = ?", (sneack_,))
    result = cur.fetchone()
    return float(result[0]) if result else None