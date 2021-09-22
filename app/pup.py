import logging
import asyncio

import telegram
import mongo


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    mongo.setup(loop)
    loop.run_until_complete(telegram.setup())
