import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('car.db')
    cur = base.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            img BLOB,
            name TEXT,
            description TEXT,
            price TEXT,
            brand TEXT,
            model TEXT
        )
    ''')
    base.commit()
    if base:
        print('Data base connected')

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('''
                    INSERT INTO menu (
                        img, name, 
                        description, 
                        price, brand, 
                        model
                    ) VALUES (?, ?, ?, ?, ?, ?)''', 
                    tuple(data.values()))
        base.commit()

async def sql_write(callback_query, item_ids):
    query = '''
            SELECT 
                img, 
                name, 
                description, 
                price 
            FROM menu WHERE ID IN 
        ({})'''.format(', '.join('?' * len(item_ids)))
    for ret in cur.execute(query, item_ids):
        photo, name, description, price = ret
        caption = f'{name}\n\n{description}\n\nЦеновая категория от {price}'
        await bot.send_photo(callback_query, photo, caption)


