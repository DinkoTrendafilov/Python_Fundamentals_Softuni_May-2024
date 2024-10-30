new_price = float(input("Enter new price of stock: "))
dividend_price = float(input("Enter dividend price of stock: "))

old_price = 18.526
shares_count = 920
clear_dividend = ((dividend_price * 0.95) / old_price) * 100
result = new_price / old_price * 100 - 100
dividend_as_value = dividend_price * 0.95 * shares_count
print("--------------------------------------------------------")
print(f"Result is: {result:.2f} %")
print(f"Dividend as percent: {clear_dividend:.2f} %")
print(f"Dividend as value: {dividend_as_value:.2f} lv.")
print("--------------------------------------------------------")
