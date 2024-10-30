group_size = int(input())
days = int(input())

total_coins = 0
avg_coins = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5

    total_coins += 50
    food_for_people = group_size * 2
    total_coins -= food_for_people

    if day % 3 == 0:
        water_for_people = group_size * 3
        total_coins -= water_for_people
    if day % 5 == 0:
        earning_money = group_size * 20
        total_coins += earning_money
        if day % 3 == 0:
            extra_cost = group_size * 2
            total_coins -= extra_cost

avg_coins = int(total_coins / group_size)
print(f"{group_size} companions received {avg_coins} coins each.")
