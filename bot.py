import argparse
from trading import place_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT)")

    args = parser.parse_args()

    print("\n📋 Order Request Summary:")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    if args.type == "LIMIT":
        print(f"Price: {args.price}")

    place_order(args.symbol, args.side, args.type, args.quantity, args.price)

if __name__ == "__main__":
    main()
