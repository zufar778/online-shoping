import logging
import asyncio
from aiogram import Dispatcher, Bot
from user import router
from config import bot_token, admins
from karzinka import k_router
from admin import a_router
from admin_add_product import adm_router

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

async def main():
    bot = Bot(token=bot_token)

    dp.include_router(adm_router)
    dp.include_router(k_router)
    dp.include_router(a_router)
    dp.include_router(router)

    try:
        for admin_id in admins:
            await bot.send_message(admin_id, "Bot ishga tushdi")

        await dp.start_polling(bot)

    except (KeyboardInterrupt, SystemExit):
        print("Bot to‘xtatildi")

    finally:
        print("Session yopilmoqda...")
        await bot.session.close()
        print("Session yopildi!")

if __name__ == "__main__":
    asyncio.run(main())
