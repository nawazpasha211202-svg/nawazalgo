# demo.py
# Simple demo script for Issue: 2-qi-02-demo-issue

import datetime
import random

def main():
    # Print a welcome message
    print("🚀 Algo Trading Demo Script Started")
    
    # Show current date and time
    now = datetime.datetime.now()
    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Simulate a random stock price
    stock_price = round(random.uniform(100, 500), 2)
    print(f"Simulated Stock Price: ${stock_price}")
    
    # Simple trading logic (demo only)
    if stock_price > 300:
        print("Decision: SELL ✅")
    else:
        print("Decision: BUY ✅")
    
    print("Demo script completed successfully!")

if __name__ == "__main__":
    main()
