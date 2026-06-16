def stock_portfolio_tracker():
    # 1. Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 170,
        "MSFT": 400
    }
    
    portfolio = {}
    total_investment = 0
    
    print("--- Stock Portfolio Tracker ---")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    # 2. Taking user input
    while True:
        symbol = input("\nStock symbol daalein (ya 'exit' likhein khatam karne ke liye): ").upper()
        if symbol == 'EXIT':
            break
        
        if symbol not in stock_prices:
            print("Ye stock hamari list mein nahi hai.")
            continue
            
        try:
            quantity = int(input(f"{symbol} ki kitni quantity hai? "))
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Kripya quantity ke liye ek valid number daalein.")

    # 3. Calculation
    print("\n--- Portfolio Summary ---")
    summary_lines = ["Stock | Quantity | Price | Total"]
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        value = price * quantity
        total_investment += value
        line = f"{symbol} | {quantity} | ${price} | ${value}"
        summary_lines.append(line)
        print(line)
        
    total_str = f"\nTotal Portfolio Investment: ${total_investment}"
    print(total_str)
    summary_lines.append(total_str)
    
    # 4. Saving to file
    save = input("\nKya aap is result ko 'portfolio.txt' mein save karna chahte hain? (y/n): ")
    if save.lower() == 'y':
        with open("portfolio.txt", "w") as f:
            f.write("\n".join(summary_lines))
        print("Result 'portfolio.txt' mein save ho gaya hai.")

# Game chalayein
stock_portfolio_tracker()