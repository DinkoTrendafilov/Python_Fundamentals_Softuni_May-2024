products = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}

    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price


for name, value in products.items():
    total_price = value["price"] * value["quantity"]
    print(f"{name} -> {total_price:.2f}")

