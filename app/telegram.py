from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

bot = Bot(token=config.TOKEN_TELEGRAM)
dp = Dispatcher(bot, storage=MemoryStorage())

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/info", description="Bot information")
    ]
    await bot.set_my_commands(commands)

async def setup():
    import handlers

    await set_commands(bot)
    await dp.skip_updates()
    await dp.start_polling()