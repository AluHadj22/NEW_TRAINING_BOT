import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('training_alu.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, callories TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()
    
async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nКалории {ret[-1]}')
