from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
token = '5126525664:AAGuOhM13q_1hslm7e1wKf3VQ6t4NkiCkvM'

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

