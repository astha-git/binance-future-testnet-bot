class ValidationError(Exception):
    """Raised when user input is invalid."""
    pass


class OrderPlacementError(Exception):
    """Raised when Binance rejects an order."""
    pass