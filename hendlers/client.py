from aiogram import types, Dispatcher
from bot import bot
from keyboards import button


#@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'ДОБРО ПОЖАЛОВАТЬ {0.first_name}\n'
                                                 'ЧЕРЕЗ ДАННОГО БОТА ВЫ МОЖЕТЕ ПОСМОТРЕТЬ МЕНЮ, РЕЖИМ РАБОТЫ А ТАК ЖЕ ЗАБРОНИРОВАТЬ СТОЛИК'.format(message.from_user),
                           reply_markup=button.mainMenu)


#@dp.message_handler(commands=['🕗 Режим работы'])
async def time_of_work(message: types.Message):
    await bot.send_message(message.from_user.id, 'Улица Чистопольская 9а\n'
                                                 'Пн-Чт 9:00-23:00\n'
                                                 'Пт-Сб 9:00-00:00\n'
                                                 'Вс 10:00-23:00')


#@dp.message_handler(commands=['📖 Меню'])
async def menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'ВЫБИРАЙТЕ С УМОМ', reply_markup=button.inlineMenu)


async def back(message: types.Message):
    await message.reply("ПЕРЕХОД НА ГЛАВНОЕ МЕНЮ", reply_markup=button.mainMenu)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start', 'help'])
    dp.register_message_handler(time_of_work, text=['🕗 РЕЖИМ РАБОТЫ'])
    dp.register_message_handler(menu, text=['📖 МЕНЮ'])
    dp.register_message_handler(back, text="🔙 НАЗАД")
    #dp.register_message_handler(bron, text=['📞 Забронировать'])
