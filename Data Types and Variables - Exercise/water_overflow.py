lines = int(input())
water_tank_capacity = 255
total_fuel = 0

for line in range(1, lines + 1):
    current_fuel = int(input())
    water_tank_capacity -= current_fuel
    if water_tank_capacity < 0:
        print("Insufficient capacity!")
        water_tank_capacity += current_fuel
        continue
    total_fuel += current_fuel

print(total_fuel)


