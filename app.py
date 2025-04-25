import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import BOT_TOKEN, ADMIN
from datetime import datetime


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),  # Запись в файл
        logging.StreamHandler()         # Вывод в консоль
    ]
)


bot = Bot(token=BOT_TOKEN)
logging.info('bot has created')

dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Hello')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
