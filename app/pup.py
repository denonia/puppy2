import logging
import asyncio

import telegram

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(telegram.setup())