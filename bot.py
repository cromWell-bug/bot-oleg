import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я помогу тебе с заказами. Введи артикул товара.")

@dp.message_handler()
async def process_article(message: types.Message):
    article = message.text
    await message.answer(f"Артикул: {article}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
