new_value = float(input("Enter a new value of stock: "))
old_value = float(input("Enter a old value of stock: "))

result = new_value / old_value * 100 - 100
# result1 = new_value / old_value * 100

print(f"Result of change is: {result:.2f} %")
# print(f"Result of change is: {result1:.2f} %")
