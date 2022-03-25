from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import button
from bot import bot


CHANNEL_ID = "@test_channel123456765"


class FSMbron(StatesGroup):
    name = State()
    time = State()
    date = State()
    people = State()
    phone_number = State()


# Начало общения с пользователем
#@dp.message_handler(text='📞 Забронировать', state=None)
async def cmd_start(message: types.Message):
    await FSMbron.name.set()
    await message.reply('👤 На чье имя забронировать столик?', reply_markup=button.nacotmBtn)


#@dp.message_handler(text=['name'], state=FSMbron.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "❌ ОТМЕНИТЬ":
            data['name'] = message.text
            await FSMbron.next()
            await message.reply('📅 На какое число забронировать столик?', reply_markup=button.dataBtn)
        else:
            await message.reply("ПЕРЕХОД НА ГЛАВНОЕ МЕНЮ", reply_markup=button.mainMenu)
            await state.finish()


#@dp.message_handler(text=['date'], state=FSMbron.date)
async def load_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
        await FSMbron.next()
        await message.reply('🕗 Во сколько подойдете?', reply_markup=button.timeBtn)


#@dp.message_handler(text=['time'], state=FSMbron.time)
async def load_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
        await FSMbron.next()
        await message.reply('👪 Сколько человек вас будет?', reply_markup=button.pepBtn)


#@dp.message_handler(text=['people'], state=FSMbron.people)
async def load_people(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['people'] = message.text
        await FSMbron.next()
        await message.reply('И на последок номер телефона пожалуйста', reply_markup=types.ReplyKeyboardRemove())


#@dp.message_handler(text=['phone_number'], state=FSMbron.phone_number)
async def load_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
        await FSMbron.next()
        await message.reply(f"Отлично!\n"
                            f"Итак, {data['time']} в {data['people']}\n"
                            f"на имя {data['name']} будем ждать вас!\n", reply_markup=button.otmBtn)


async def cencel_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "✅ ДА":
            await message.reply("Бронь принята", reply_markup=button.mainMenu)
            await bot.send_message(CHANNEL_ID, f"Бронь:\n"
                                            f"Ф.И.О: {data['name']}\n"
                                            f"Время: {data['people']}\n"
                                            f"Дата: {data['time']}\n"
                                            f"Кол-во гостей: {data['date']}\n"
                                            f"Номер телефона: {data['phone_number']}")
        elif message.text == "❌ НЕТ":
            await bot.send_message(message.from_user.id, "Бронь отменена", reply_markup=button.mainMenu)
        await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cmd_start, text='📞 ЗАБРОНИРОВАТЬ', state=None)
    dp.register_message_handler(load_name, state=FSMbron.name)
    dp.register_message_handler(load_date, state=FSMbron.date)
    dp.register_message_handler(load_time, state=FSMbron.time)
    dp.register_message_handler(load_people, state=FSMbron.people)
    dp.register_message_handler(load_phone_number, state=FSMbron.phone_number)
    dp.register_message_handler(cencel_message)
