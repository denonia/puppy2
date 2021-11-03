from asyncio.events import AbstractEventLoop
from utils.mongo_repository import MongoRepository


def setup(loop: AbstractEventLoop) -> None:
    global repository
    repository = MongoRepository(loop)
