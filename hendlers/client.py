from aiogram import types, Dispatcher
from bot import bot
from keyboards import button

CHANNEL_ID = "@test_channel123456765"


def check_admin(chat_member):
    if chat_member['status'] == 'administrator' or chat_member['status'] == 'creator':
        return True
    else:
        return False

def check_message(message):


# @dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    if check_admin(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Функции для МОДЕРАТОРА", reply_markup=button.btnAdm)
    else:
        await bot.send_message(message.from_user.id, 'ДОБРО ПОЖАЛОВАТЬ {0.first_name}\n'
                                                     'ЧЕРЕЗ ДАННОГО БОТА ВЫ МОЖЕТЕ ПОСМОТРЕТЬ МЕНЮ, РЕЖИМ РАБОТЫ А ТАК ЖЕ ЗАБРОНИРОВАТЬ СТОЛИК'.format(
            message.from_user),
                               reply_markup=button.mainMenu)


async def check_bron(message: types.Message):
    if message.text == "❌ Остоновить брони":
        await message.reply("Брони пока не принимаются", reply_markup=button.btnAdm)
    else:
        await message.reply("Пора работать!", reply_markup=button.btnAdm)


# @dp.message_handler(commands=['🕗 Режим работы'])
async def time_of_work(message: types.Message):
    await bot.send_message(message.from_user.id, 'Улица Аделя Кутуя 68/2\n'
                                                 'Пн-Чт 9:00-23:00\n'
                                                 'Пт-Сб 9:00-00:00\n'
                                                 'Вс 10:00-23:00')


# @dp.message_handler(commands=['📖 Меню'])
async def menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'ВЫБИРАЙТЕ С УМОМ', reply_markup=button.inlineMenu)


async def back(message: types.Message):
    await message.reply("ПЕРЕХОД НА ГЛАВНОЕ МЕНЮ", reply_markup=button.mainMenu)


"""Блок команд после открытие МЕНЮ"""


async def gor_zak(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/Menyu-03-26-3", reply_markup=button.inlineMenu)


"""Блок для модератора"""



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start', 'help'])
    dp.register_message_handler(time_of_work, text=['🕗 РЕЖИМ РАБОТЫ'])
    dp.register_message_handler(menu, text=['📖 МЕНЮ'])
    dp.register_message_handler(back, text="🔙 НАЗАД")
    """Блок открытие меню"""
    dp.register_message_handler(gor_zak, text="🍱 ХОЛОДНЫЕ И ГОРЯЧИЕ ЗАКУСКИ")
    """Блок для модератора"""
    dp.register_message_handler(check_bron, text="❌ Остоновить брони")
