from aiogram.types import Message
from utils.dimon import save_msg_to_buffer


async def dimon_handler(message: Message) -> None:
    await save_msg_to_buffer(message.text)
