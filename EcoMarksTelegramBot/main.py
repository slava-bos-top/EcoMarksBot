import asyncio

from aiogram import Bot, Dispatcher
from app.hendlers import router
from config import Config


Config.load()
bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот вимкнено!")
