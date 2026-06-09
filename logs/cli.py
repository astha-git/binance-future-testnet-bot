import argparse

from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
)
from bot.logging_config import setup_logging


logger = setup_logging()


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        symbol = validate_symbol(
            args.symbol
        )

        side = validate_side(
            args.side
        )

        order_type = validate_order_type(
            args.type
        )

        quantity = validate_quantity(
            args.quantity
        )

        if (
            order_type == "LIMIT"
            and args.price is None
        ):
            raise ValueError(
                "LIMIT orders require --price"
            )

        client = (
            BinanceFuturesClient()
            .get_client()
        )

        service = OrderService(client)

        response = service.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=args.price,
        )

        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if args.price:
            print(f"Price: {args.price}")

        print("\n===== RESPONSE =====")
        print(
            f"Order ID: {response.get('orderId')}"
        )

        print(
            f"Status: {response.get('status')}"
        )

        print(
            f"Executed Qty: {response.get('executedQty')}"
        )

        avg_price = response.get(
            "avgPrice",
            "N/A"
        )

        print(
            f"Average Price: {avg_price}"
        )

        print("\n✓ Order placed successfully")

    except Exception as e:

        logger.exception(str(e))

        print(
            f"\n✗ Order failed: {e}"
        )


if __name__ == "__main__":
    main()