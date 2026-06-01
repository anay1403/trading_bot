from binance.exceptions import BinanceAPIException
from binance_client import get_client
from logger import setup_logger

logger = setup_logger()
client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Placing {side} {order_type} order: {quantity} {symbol} at {price if price else 'MARKET'}")

        if order_type.upper() == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        elif order_type.upper() == "LIMIT":
            if not price:
                raise ValueError("Price required for LIMIT order")
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
        else:
            raise ValueError("Invalid order type. Use MARKET or LIMIT.")

        logger.info(f"Order response: {order}")
        print("\nOrder placed successfully!")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")
        print(f"Executed Qty: {order['executedQty']}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")
        return order

    except BinanceAPIException as e:
        logger.error(f"API Error: {e}")
        print(f"API Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        print(f"Unexpected Error: {e}")
