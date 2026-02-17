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
        for id in admins:
            await bot.send_message(chat_id=id, text="bot ishga tushdi")

        await dp.start_polling(bot)

    finally:
        await bot.session.close()   # 🔥 MUHIM QATOR

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to‘xtadi")
