import math

bisquits_per_person_per_day = int(input())
workers_count = int(input())
number_of_bisquits_per_30_days = int(input())

total_production = 0
daily_production = 0
for day in range(1, 31):
    if day % 3 == 0:
        daily_production = workers_count * bisquits_per_person_per_day * 0.75
    else:
        daily_production = workers_count * bisquits_per_person_per_day
    total_production += math.floor(daily_production)

diff = total_production - number_of_bisquits_per_30_days
diff_percentage = abs((diff) / number_of_bisquits_per_30_days) * 100

print(f"You have produced {total_production} biscuits for the past month.")

if total_production > number_of_bisquits_per_30_days:
    print(f"You produce {diff_percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {diff_percentage:.2f} percent less biscuits.")
