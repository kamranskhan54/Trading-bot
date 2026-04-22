import logging
from typing import Dict, Optional
from bot.client import BinanceFuturesClient
from bot.validators import validate_order_params

logger = logging.getLogger(__name__)

class OrderManager:
    """Manages order placement and validation"""
    
    def __init__(self, client: BinanceFuturesClient):
        self.client = client
    
    def place_order(self, symbol: str, side: str, order_type: str, 
                   quantity: float, price: Optional[float] = None) -> Dict:
        """
        Place an order with validation
        
        Args:
            symbol: Trading pair (e.g., BTCUSDT)
            side: BUY or SELL
            order_type: MARKET or LIMIT
            quantity: Order quantity
            price: Price (required for LIMIT orders)
        
        Returns:
            API response dictionary
        """
        # Validate inputs
        validate_order_params(symbol, side, order_type, quantity, price)
        
        # Build order parameters
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }
        
        logger.info(f"Validated order parameters - Symbol: {symbol}, Side: {side}, Type: {order_type}, Qty: {quantity}, Price: {price}")
        logger.info(f"Placing {order_type} order: {params}")
        
        if order_type == 'LIMIT':
            params['timeInForce'] = 'GTC'
            params['price'] = price
        
        # Place order
        response = self.client.place_order(**params)
        logger.info("Order placement completed successfully")
        
        return response
