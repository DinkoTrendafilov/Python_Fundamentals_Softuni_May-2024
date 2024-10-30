new_price = float(input("Enter new price of stock: "))

old_price = 18.526
stock_count = 920
invested_money = old_price * stock_count
current_money = new_price * stock_count
clear_dividend = 0.60 * 0.95 * stock_count
profit = (current_money - invested_money) + clear_dividend
result = new_price / old_price * 100 - 100

print()
print(f"Result of change is: {result:.2f} %")
print()
print(f"Total invested money: {int(invested_money):_} lv ")
print(f"Current state of money: {int(current_money):_} lv ")
print(f"Profit of investments are: {int(profit):_} lv ")
print(f"Clear dividend money: {int(clear_dividend):_} lv ")
