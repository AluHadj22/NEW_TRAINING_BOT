from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/menu')
b4 = KeyboardButton('/calories')
b5 = KeyboardButton('/Train')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b3).add(b2).insert(b4).insert(b5)
