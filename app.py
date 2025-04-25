import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import handlers



async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),  # Запись в файл
            logging.StreamHandler()  # Вывод в консоль
        ]
    )

    bot = Bot(token=BOT_TOKEN)
    logging.info('bot has created')
    dp = Dispatcher()

    dp.include_routers(handlers.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
