from telegram import dp
from aiogram.types import ContentType, Message

from services.demot import reply_handler
from services.dimon import dimon_handler

# it's actually my id..
DIMON_ID = 305873506


@dp.message_handler(content_types=ContentType.TEXT)
async def handle_message(message: Message) -> None:
    if message.reply_to_message and "|" in message.text:
        await reply_handler(message)
    if message.from_user.id == DIMON_ID and len(message.text) > 2:
        await dimon_handler(message)
