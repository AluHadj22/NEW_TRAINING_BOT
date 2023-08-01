from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = 'YOUR TOKEN'
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)
