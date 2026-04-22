# Trading Bot - Binance Futures Testnet

A professional Python trading bot for placing orders on **Binance Futures Testnet (USDT-M)** with comprehensive logging, validation, and error handling.

## 🎯 Features

✅ **Market & Limit Orders** - Full support for both order types  
✅ **BUY & SELL** - Both sides implemented  
✅ **Input Validation** - Comprehensive parameter validation  
✅ **Professional Logging** - File and console logging with rotation  
✅ **Error Handling** - API errors, network errors, validation errors  
✅ **Clean Architecture** - Separation of concerns (client, orders, CLI)  
✅ **CLI Interface** - Easy-to-use command-line interface  

## 📋 Requirements

- Python 3.8+
- Binance Futures Testnet account
- API credentials (API Key + Secret)

## 🚀 Setup

### 1. Clone Repository
```bash
git clone https://github.com/kamranskhan54/trading-bot.git
cd trading-bot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Credentials
```bash
cp .env.example .env
```

Edit `.env` with your Binance Futures Testnet credentials:
```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

## 📚 Getting Binance Testnet Credentials

1. Visit: https://testnet.binancefuture.com
2. Register or login
3. Go to API Management
4. Create new API key (copy both API Key and Secret)
5. Add to `.env` file

## 💻 Usage

### Place a Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 1.0 --price 2500.50
```

### Supported Symbols
- BTCUSDT
- ETHUSDT
- BNBUSDT
- ADAUSDT
- XRPUSDT
- DOGEUSDT

### CLI Help
```bash
python cli.py --help
```

## 📂 Project Structure

```
trading-bot/
├── bot/
│   ├── __init__.py              # Package initialization
│   ├── client.py                # Binance API wrapper
│   ├── orders.py                # Order management logic
│   ├── validators.py            # Input validation
│   └── logging_config.py         # Logging configuration
├── cli.py                        # CLI entry point
├── requirements.txt              # Python dependencies
├── .env.example                  # API credentials template
├── .gitignore                    # Git ignore file
├── logs/                         # Log files directory
│   ├── sample_market_order.log   # Sample MARKET order log
│   └── sample_limit_order.log    # Sample LIMIT order log
└── README.md                     # This file
```

## 📝 Logging

Logs are saved to `logs/trading_bot.log` with:
- **File logging**: All DEBUG and above messages (rotating, 10MB max)
- **Console logging**: INFO and above messages

### Sample Log Output
```
2026-04-22 14:32:17 - trading_bot - INFO - BinanceFuturesClient initialized
2026-04-22 14:32:17 - trading_bot - INFO - Validated order parameters - Symbol: BTCUSDT, Side: BUY, Type: MARKET
2026-04-22 14:32:17 - trading_bot - INFO - Order placed successfully. Response: {...}
```

## ✅ Validation

The bot validates:
- ✅ Symbol is in supported list
- ✅ Side is BUY or SELL
- ✅ Order type is MARKET or LIMIT
- ✅ Quantity is positive number
- ✅ Price is provided for LIMIT orders

## 🔒 Security

- API credentials stored in `.env` (not committed to git)
- `.gitignore` prevents accidental credential leaks
- HMAC-SHA256 signature for all requests

## 🛠️ Error Handling

Handles:
- Invalid input parameters
- API errors (4xx, 5xx)
- Network timeouts
- Missing credentials

## 🎓 Code Quality

- **Clean Architecture**: Separation of concerns
- **Type Hints**: Better code documentation
- **Comprehensive Logging**: Easy debugging
- **Professional Error Handling**: User-friendly messages

## 📝 Assumptions

1. Binance Futures Testnet is available
2. API credentials are valid
3. Account has sufficient balance for orders
4. Network connectivity is stable

## 🤝 Support

For issues with Binance Testnet:
- Visit: https://testnet.binancefuture.com
- Check API docs: https://binance-docs.github.io/apidocs/
