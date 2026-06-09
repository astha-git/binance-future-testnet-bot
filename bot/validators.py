from .exceptions import ValidationError


def validate_symbol(symbol: str) -> str:

    symbol = symbol.upper()

    if not symbol.endswith("USDT"):
        raise ValidationError(
            "Only USDT pairs are supported."
        )

    return symbol


def validate_side(side: str) -> str:

    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValidationError(
            "Side must be BUY or SELL."
        )

    return side


def validate_order_type(order_type: str) -> str:

    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValidationError(
            "Order type must be MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity: float):

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than zero."
        )

    return quantity