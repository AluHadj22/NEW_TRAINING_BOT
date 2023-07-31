from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '6581826705:AAF-moUaDlLo3BmN7FkthvQ54Xqq5OBBrRI'
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)
