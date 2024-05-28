import os
import time

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers.users_handler import users_router
from middleware import SessionMiddleware

load_dotenv()

bot = Bot(token=os.environ.get('TOKEN'), parse_mode=ParseMode.HTML)
dp = Dispatcher()

dp.include_router(users_router)


async def on_startup():
    print('Bot started...')


async def main():
    dp.startup.register(on_startup)
    # dp.update.middleware(CounterMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.set_my_commands(bot_cmds, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == '__main__':
    # while True:
    #     try:
    asyncio.run(main())
    # except Exception as e:
    #     print(f"Exception: {e}")
    #     time.sleep(15)
