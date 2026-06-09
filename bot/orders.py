import logging

from binance.exceptions import (
    BinanceAPIException,
    BinanceRequestException,
)

from .exceptions import OrderPlacementError


class OrderService:

    def __init__(self, client):

        self.client = client
        self.logger = logging.getLogger(
            "trading_bot"
        )

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None,
    ):

        try:

            request_data = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":

                request_data["price"] = price
                request_data["timeInForce"] = "GTC"

            self.logger.info(
                f"ORDER REQUEST: {request_data}"
            )

            response = self.client.futures_create_order(
                **request_data
            )

            self.logger.info(
                f"ORDER RESPONSE: {response}"
            )

            return response

        except BinanceAPIException as e:

            self.logger.error(
                f"Binance API Error: {e}"
            )

            raise OrderPlacementError(str(e))

        except BinanceRequestException as e:

            self.logger.error(
                f"Network Error: {e}"
            )

            raise OrderPlacementError(str(e))