import logging
from typing import Optional

logger = logging.getLogger(__name__)

VALID_SYMBOLS = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'ADAUSDT', 'XRPUSDT', 'DOGEUSDT']
VALID_SIDES = ['BUY', 'SELL']
VALID_TYPES = ['MARKET', 'LIMIT']

class ValidationError(Exception):
    """Custom validation error"""
    pass

def validate_order_params(symbol: str, side: str, order_type: str, 
                         quantity: float, price: Optional[float] = None) -> None:
    """
    Validate order parameters
    
    Raises:
        ValidationError: If any parameter is invalid
    """
    # Validate symbol
    if not symbol or not isinstance(symbol, str):
        raise ValidationError("Symbol must be a non-empty string")
    if symbol.upper() not in VALID_SYMBOLS:
        raise ValidationError(f"Invalid symbol: {symbol}. Supported: {', '.join(VALID_SYMBOLS)}")
    
    # Validate side
    if side.upper() not in VALID_SIDES:
        raise ValidationError(f"Side must be BUY or SELL, got: {side}")
    
    # Validate order type
    if order_type.upper() not in VALID_TYPES:
        raise ValidationError(f"Order type must be MARKET or LIMIT, got: {order_type}")
    
    # Validate quantity
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValidationError(f"Quantity must be a positive number, got: {quantity}")
    
    # Validate price for LIMIT orders
    if order_type.upper() == 'LIMIT':
        if price is None or price <= 0:
            raise ValidationError("Price is required and must be positive for LIMIT orders")
    
    logger.debug(f"Validation passed for {symbol} {side} {order_type}")
