from typing import List
from mongo import repository

msg_buffer: List[str] = []


async def save_msg_to_buffer(message: str) -> None:
    msg_buffer.append(message)
    if len(msg_buffer) > 10:
        await send_msg_to_rep()


async def send_msg_to_rep() -> None:
    print("piu..", end=" ")
    print(msg_buffer)
    if len(msg_buffer) == 0:
        return
    await repository.save(msg_buffer)
    msg_buffer.clear()
