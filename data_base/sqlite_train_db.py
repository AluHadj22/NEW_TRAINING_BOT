import sqlite3 as sq
from create_bot import bot


def sql_start_train():
    base = sq.connect('training_alu_train.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    
    cur.execute('CREATE TABLE IF NOT EXISTS Train(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, link TEXT)')
    base.commit()
    base.close()

async def sql_add_command_training(state):
    link = state.get('link')
    name = state.get('name')
    description = state.get('description')

    if link and name and description:
        base = sq.connect('training_alu_train.db')
        cur = base.cursor()
        cur.execute('INSERT INTO Train (name, description, link) VALUES (?, ?, ?)', (name, description, link))
        base.commit()
        base.close()

async def sql_read(message):
    base = sq.connect('training_alu_train.db')
    cur = base.cursor()
    for ret in cur.execute('SELECT * FROM Train').fetchall():
        name = ret[1]
        description = ret[2]
        link = ret[3]
        await send_video_or_link(message.chat.id, name, description, link)
    base.close()

async def send_video_or_link(chat_id, name, description, link):
    if link.startswith('http'):  # Проверяем, является ли ссылка URL-адресом
        await bot.send_message(chat_id, f"Название: {name}\nОписание: {description}\nСсылка: {link}")  # Отправляем ссылку как сообщение
    else:
        await bot.send_video(chat_id, link, caption=f"Название: {name}\nОписание: {description}")  # Отправляем видео с заголовком и описанием
