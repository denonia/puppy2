from typing import List
from motor import motor_asyncio
from config import MONGODB_ATLAS_URL
from asyncio import events


class MongoRepository(object):
    def __init__(self, loop: events.AbstractEventLoop):
        global mongo
        client: motor_asyncio.AsyncIOMotorClient = motor_asyncio.AsyncIOMotorClient(MONGODB_ATLAS_URL, io_loop=loop)
        print(client.server_info())
        mongo = client["dima_msg"]["messages"]

    async def save(self, messages: List[str]) -> None:
        await mongo.insert_many([{"message": message} for message in messages])

    async def get(self) -> List[str]:
        result = await mongo.find({})
        return result["message"]
