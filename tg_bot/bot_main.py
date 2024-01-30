import os
import sys

import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart

sys.path.insert(0, os.path.join(os.getcwd()))

if __name__ == "__main__":
    from core.db.config import settings


dp = Dispatcher()


@dp.message(CommandStart)
async def handle_start(message: types.Message):
    await message.answer(
        f"Здравствуй {message.from_user.full_name} {message.from_user.id}"
    )


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == "__main__":
    bot = Bot(token=settings.BOT_TOKEN)
    asyncio.run(main())
