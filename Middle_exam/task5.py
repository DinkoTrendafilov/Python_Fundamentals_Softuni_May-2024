days = int(input())
daily_win = int(input())
target_value = float(input())

total_win = 0

for day in range(1, days + 1):
    total_win += daily_win
    if day % 3 == 0:
        total_win += daily_win * 0.5
    if day % 5 == 0:
        total_win *= 0.7

win_as_percent = total_win / target_value * 100

if total_win >= target_value:
    print("Yes, you achieve target value")
    print(f"You win {total_win:.2f} total money")
else:
    print("No, you can not achieve target value")
    print(f"You win {total_win:.2f} total money, that is {win_as_percent:.2f} % of target value")
