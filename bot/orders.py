import logging
import json
from binance.exceptions import BinanceAPIException, BinanceRequestException
from .exceptions import OrderPlacementError


class OrderService:

    def __init__(self, client):
        self.client = client
        self.logger = logging.getLogger("trading_bot")

    def place_order(self, symbol, side, order_type, quantity, price=None):

        try:
            request_data = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": str(quantity)
            }

            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("LIMIT order requires price")

                request_data["price"] = str(price)
                request_data["timeInForce"] = "GTC"

            self.logger.info("ORDER REQUEST: %s", json.dumps(request_data, indent=2))

            response = self.client.futures_create_order(**request_data)

            self.logger.info("ORDER RESPONSE: %s", json.dumps(response, indent=2))

            if not response or "orderId" not in response:
                self.logger.error(f"Invalid response from Binance: {response}")
                raise OrderPlacementError(f"Invalid response: {response}")

            return response

        except BinanceAPIException as e:
            self.logger.error(f"Binance API Error: {e}")
            raise OrderPlacementError(str(e))

        except BinanceRequestException as e:
            self.logger.error(f"Network Error: {e}")
            raise OrderPlacementError(str(e))

        except Exception as e:
            self.logger.error(f"Unexpected Error: {e}")
            raise OrderPlacementError(str(e))