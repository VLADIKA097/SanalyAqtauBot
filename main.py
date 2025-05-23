import logging
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🌳 Добавить дерево", "📢 Объявления")
    markup.add("⭐ Отзывы", "🚡 Безопасность")
    markup.add("🎯 Колесо удачи", "👤 Профиль")
    await message.answer("Добро пожаловать в SanalyAqtauBot!\nВыберите раздел:", reply_markup=markup)

@dp.message_handler(lambda msg: msg.text == "👤 Профиль")
async def profile(msg: types.Message):
    await msg.reply("Ваш профиль:\nИмя: {0}\nБаллы: 120\nУровень: 🌱 Новичок".format(msg.from_user.username))

@dp.message_handler(lambda msg: msg.text == "🎯 Колесо удачи")
async def fortune(msg: types.Message):
    await msg.reply("Вы крутанули колесо и получили +10 баллов!")