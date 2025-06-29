import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.getenv("TOKEN")  # <-- токен из переменной окружения

bot = Bot(token=TOKEN)
dp = Dispatcher()  # вот тут создаём диспетчер

@dp.message(Command("start"))
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть LMS",
            web_app=WebAppInfo(url="https://minilms-git-main-evgenii-timofeevs-projects.vercel.app")
        )]
    ])
    await message.answer("Привет! Нажми кнопку ниже, чтобы открыть LMS:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)  # передаём bot в start_polling

if __name__ == "__main__":
    asyncio.run(main())
