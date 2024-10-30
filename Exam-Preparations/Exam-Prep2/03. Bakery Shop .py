foods = {}
total_sold_quantities = 0

while True:
    command = input()
    if command == "Complete":
        break

    split_command = command.split()
    action = split_command[0]
    quantity = int(split_command[1])
    food = split_command[2]

    if action == "Receive":
        if quantity <= 0:
            continue
        if food not in foods:
            foods[food] = quantity
        else:
            foods[food] += quantity

    elif action == "Sell":
        if food not in foods:
            print(f"You do not have any {food}.")
            continue

        if quantity > foods[food]:
            sold_quantity = foods[food]
            total_sold_quantities += sold_quantity
            print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
            del foods[food]

        else:
            foods[food] -= quantity
            total_sold_quantities += quantity
            if foods[food] == 0:
                print(f"You sold {quantity} {food}.")
                del foods[food]
            else:
                print(f"You sold {quantity} {food}.")

for key, value in foods.items():
    print(f"{key}: {value}")

print(f"All sold: {total_sold_quantities} goods")
