products = {}

while True:
    command = input()
    if command == "statistics":
        break
    split_command = command.split(": ")
    product_name = split_command[0]
    product_quantity = int(split_command[1])

    if product_name not in products:
        products[product_name] = product_quantity
    else:
        products[product_name] += product_quantity

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
