number_of_orders = int(input())
total_price = 0
order_price = 0

for _ in range(1, number_of_orders + 1):
    capsule_price = float(input())
    days = int(input())
    capsules_per_days = int(input())
    if ((capsule_price < 0.01 or capsule_price > 100)
            or (days < 1 or days > 31)
            or capsules_per_days < 1 or capsules_per_days > 2_000):
        continue
    order_price = capsule_price * days * capsules_per_days
    print(f"The price for the coffee is: ${order_price:.2f}")
    total_price += order_price

print(f"Total: ${total_price:.2f}")
