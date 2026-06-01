# Binance Futures Testnet Trading Bot

## Objective
A simplified Python bot that places Market and Limit orders on Binance Futures Testnet (USDT-M).  
Supports BUY and SELL, CLI input, structured code, logging, and error handling.

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/anay1403/trading_bot.git
   cd trading_bot
2. Create a virtual environment:
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
3. Install Dependencies:
    pip install -r requirements.txt

4. Add your API Key + Secret in config.py.

HOW TO RUN:
Market Order:
python bot.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Limit Order:
python bot.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

Assumptions:
1. Using Binance Futures Testnet (https://testnet.binancefuture.com).
2. API keys are valid and have Futures permissions.
3. Orders are small (e.g., 0.001 BTCUSDT) for demo purposes.
4. LIMIT orders require a --price argument.

Requirements:
Python 3.9+
Dependencies listed in requirements.txt

Logs:
All API requests and responses are logged to trading.log.

Example Market Order:
📋 Order Request Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001
2026-06-01 16:51:02,135 - INFO - Placing BUY MARKET order: 0.001 BTCUSDT at MARKET
2026-06-01 16:51:02,628 - INFO - Order response: {'orderId': 13690487596, 'symbol': 'BTCUSDT', 'status': 'NEW', ... }
✅ Order placed successfully!
Order ID: 13690487596
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00

Example Limiy Order:
📋 Order Request Summary:
Symbol: BTCUSDT
Side: SELL
Type: LIMIT
Quantity: 0.001
Price: 70000
2026-06-01 16:55:10,421 - INFO - Placing SELL LIMIT order: 0.001 BTCUSDT at 70000
2026-06-01 16:55:10,890 - INFO - Order response: {'orderId': 13690512345, 'symbol': 'BTCUSDT', 'status': 'NEW', ... }
✅ Order placed successfully!
Order ID: 13690512345
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00
