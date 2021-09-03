import time

from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

start_time = time.time()

bot = Bot(token=config.TOKEN_TELEGRAM)
dp = Dispatcher(bot, storage=MemoryStorage())


async def set_commands(bot: Bot) -> None:
    commands = [BotCommand(command="/stats", description="Bot stats")]
    await bot.set_my_commands(commands)


async def setup() -> None:
    import handlers

    await set_commands(bot)
    await dp.skip_updates()
    await dp.start_polling()
