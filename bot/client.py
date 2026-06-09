import os

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


class BinanceFuturesClient:

    TESTNET_URL = "https://testnet.binancefuture.com"

    def __init__(self):

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError(
                "Missing Binance API credentials."
            )

        self.client = Client(
            api_key,
            api_secret
        )

        self.client.FUTURES_URL = self.TESTNET_URL

    def get_client(self):
        return self.client