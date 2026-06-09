import logging
from pathlib import Path


def setup_logging():

    Path("logs").mkdir(exist_ok=True)

    logging.basicConfig(
        filename="logs/trading_bot.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    return logging.getLogger("trading_bot")