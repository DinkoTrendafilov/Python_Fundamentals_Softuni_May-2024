dice_list = []
dice_keys = [num for num in range(6, 37)]
dice_values = [0 for num in range(6, 37)]
dice_dictionary = dict(zip(dice_keys, dice_values))

for num1 in range(1, 7):
    for num2 in range(1, 7):
        for num3 in range(1, 7):
            for num4 in range(1, 7):
                for num5 in range(1, 7):
                    for num6 in range(1, 7):
                        result = num1 + num2 + num3 + num4 + num5 + num6
                        dice_list.append(result)


for num in dice_list:
    if num not in dice_dictionary:
        dice_dictionary[num] = 1
    else:
        dice_dictionary[num] += 1

total_combinations = 6 * 6 * 6 * 6 * 6 * 6
result_as_percent = (1 / total_combinations) * 100
total_combinations = "{:,}".format(total_combinations).replace(",", "_")

sorted_dice_dictionary = dict(sorted(dice_dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

total = 0
for key, value in sorted_dice_dictionary.items():
    total += result_as_percent * value
    print(f"Key is: {key:02d} -> Value is: {value:02d} = {result_as_percent * value:.2f}%")

print(f"Total combination are: {total_combinations} total result is: {total:.2f}%")
