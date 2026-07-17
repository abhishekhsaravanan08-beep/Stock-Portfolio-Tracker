# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 350,
    "AMZN": 140
}

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

# Get number of different stocks
num_stocks = int(input("Enter the number of different stocks: "))

# Total investment value
total_investment = 0

# Create a text file
file = open("portfolio.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("==============================\n")
file.write("Stock\tQuantity\tPrice\tValue\n")

# Get stock details
for i in range(num_stocks):
    stock = input("\nEnter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        price = stock_prices[stock]
        value = price * quantity
        total_investment += value

        print(f"{stock}: {quantity} × ${price} = ${value}")

        file.write(f"{stock}\t{quantity}\t\t${price}\t${value}\n")

    else:
        print("Invalid stock name!")

# Save total investment
file.write("==============================\n")
file.write(f"Total Investment Value: ${total_investment}\n")
file.close()

# Display total investment
print("\n===================================")
print(f"Total Investment Value = ${total_investment}")
print("Portfolio saved successfully in 'portfolio.txt'")
print("===================================")