from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp,bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from data_base import sqlite_train_db
from keybord_client import menu_kb
from aiogram.dispatcher.filters import Text

ID = None


class Training(StatesGroup):
    waiting_for_name = State()
    waiting_for_description = State()
    waiting_for_link = State()

#ПОЛУЧАЮ ID ТЕКУЩЕГО МОДЕРА
@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что вы хотите сделать?', reply_markup=menu_kb.button_case_admin)
    await message.delete()

@dp.message_handler(commands=['load_TRAINING'])
async def start_training(message: types.Message):
    await message.answer("Пожалуйста, напишите название видео")
    await Training.waiting_for_name.set()
#Выход из состояний
@dp.message_handler(state="*", commands=['cancel'])
@dp.message_handler(Text(equals='cancel', ignore_case=True),state='*')
async def cancel_handler(message: types.Message,  state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.finish()
    await message.reply('OK')

@dp.message_handler(state=Training.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Пожалуйста, напишите описание видео")
    await Training.waiting_for_description.set()

@dp.message_handler(state=Training.waiting_for_description)
async def process_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    await message.answer("Пожалуйста, пришлите ссылку на видео с тренировкой")
    await Training.waiting_for_link.set()

@dp.message_handler(state=Training.waiting_for_link)
async def process_link(message: types.Message, state: FSMContext):
    link = message.text
    async with state.proxy() as data:
        data['link'] = link
        data_dict = dict(data)
    await sqlite_train_db.sql_add_command_training(data_dict)
    await state.finish()
    await message.answer("Спасибо! Ссылка на тренировку сохранена.")

def register_handlers_training(dp: Dispatcher):
    dp.register_message_handler(start_training, commands=['load_TRAINING'])
    dp.message_handler(state="*", commands=['cancel'])
    dp.message_handler(Text(equals='cancel', ignore_case=True),state='*')
    dp.register_message_handler(process_name, state=Training.waiting_for_name)
    dp.register_message_handler(process_description, state=Training.waiting_for_description)
    dp.register_message_handler(process_link, state=Training.waiting_for_link)
   