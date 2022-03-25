from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


"""inline menu"""
btnbar = KeyboardButton("🍾 Бар")
btnkitchen = KeyboardButton("🍲 Кухня")
btndes = KeyboardButton("🍮 Десерты")
btnbzn = KeyboardButton("🥡 Бизнес-ланч")
btnnaz = KeyboardButton("🔙 Назад")
inlineMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnbar, btnkitchen, btnbzn, btndes, btnnaz)