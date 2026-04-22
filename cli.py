import argparse
import logging
import os
from dotenv import load_dotenv
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import ValidationError
from bot.logging_config import setup_logging

# Setup logging
setup_logging()
logger = logging.getLogger('trading_bot')

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
  python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 1.0 --price 2500.50
        """
    )
    
    parser.add_argument('--symbol', required=True, help='Trading pair (e.g., BTCUSDT)')
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--type', required=True, dest='order_type', choices=['MARKET', 'LIMIT'], help='Order type')
    parser.add_argument('--quantity', type=float, required=True, help='Order quantity')
    parser.add_argument('--price', type=float, help='Order price (required for LIMIT orders)')
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    if not api_key or not api_secret:
        logger.error("API credentials not found in .env file")
        print("❌ Error: Missing API credentials in .env file")
        print("Please create .env file with BINANCE_API_KEY and BINANCE_API_SECRET")
        return
    
    try:
        # Initialize client and manager
        client = BinanceFuturesClient(api_key, api_secret)
        manager = OrderManager(client)
        
        # Print order summary
        print("\n" + "="*60)
        print("📊 ORDER REQUEST SUMMARY")
        print("="*60)
        print(f"Symbol:      {args.symbol}")
        print(f"Side:        {args.side}")
        print(f"Type:        {args.order_type}")
        print(f"Quantity:    {args.quantity}")
        if args.price:
            print(f"Price:       {args.price}")
        print("="*60 + "\n")
        
        # Place order
        response = manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )
        
        # Print response
        print("="*60)
        print("✅ ORDER RESPONSE DETAILS")
        print("="*60)
        print(f"Order ID:      {response.get('orderId')}")
        print(f"Status:        {response.get('status')}")
        print(f"Executed Qty:  {response.get('executedQty')}")
        if response.get('avgPrice'):
            print(f"Avg Price:     {response.get('avgPrice')}")
        print("="*60)
        print("✅ Success: Order placed successfully!\n")
        
    except ValidationError as e:
        logger.error(f"Validation error: {str(e)}")
        print(f"\n❌ Validation Error: {str(e)}\n")
    except Exception as e:
        logger.error(f"Failed to place order: {str(e)}", exc_info=True)
        print(f"\n❌ Error: {str(e)}\n")

if __name__ == "__main__":
    main()
