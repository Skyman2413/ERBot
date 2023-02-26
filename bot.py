# coding: utf8
import asyncio
import logging
import pathlib

from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import root_handler, book_info, faq_handler, services_handler, unhandled


async def main():
    path = str(pathlib.Path(pathlib.Path.cwd(), "logs", "log.txt"))
    logging.basicConfig(level=logging.INFO, filename=path)
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(root_handler.router)
    dp.include_router(book_info.router)
    dp.include_router(services_handler.router)
    dp.include_router(faq_handler.router)
    dp.include_router(unhandled.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
