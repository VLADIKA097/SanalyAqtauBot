
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("🌳 Добавить дерево"))
main_menu.add(KeyboardButton("📢 Объявления"), KeyboardButton("⭐ Отзывы"))
main_menu.add(KeyboardButton("🚡 Безопасность"), KeyboardButton("🎯 Колесо удачи"))
main_menu.add(KeyboardButton("👤 Профиль"))

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    username = message.from_user.username or "Пользователь"
    welcome_text = f"Привет, {username}! Добро пожаловать в SanalyAqtauBot!"
    if username == "vladik97":
        welcome_text += "\n\nВы отмечены как 👑 Создатель проекта!"
    await message.answer(welcome_text, reply_markup=main_menu)

@dp.message_handler(lambda m: m.text == "👤 Профиль")
async def profile_handler(message: types.Message):
    await message.answer(f"Ваш профиль:\nИмя: {message.from_user.username or 'Пользователь'}\nБаллы: 120\nУровень: 🌱 Новичок")

@dp.message_handler(lambda m: m.text == "🎯 Колесо удачи")
async def luck_handler(message: types.Message):
    await message.answer("Вы крутанули колесо и получили +10 баллов!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
