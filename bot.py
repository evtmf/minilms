import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "7350288182:AAHnYYdNaoq5LY2Wxnwnt94m0bHKZnSdd0E"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть LMS",
            web_app=WebAppInfo(url="https://nextjs-boilerplate-o1o03ku2d-evgenii-timofeevs-projects.vercel.app")  # замени своей ссылкой
        )]
    ])
    await message.answer("Привет! Нажми кнопку ниже, чтобы открыть LMS:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
