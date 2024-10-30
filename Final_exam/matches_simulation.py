import random

number_of_matches = int(input("Enter number of matches: "))
player_numbers = [num for num in input(f"Enter your {number_of_matches} numbers: ").split()]
dictionary_total_find_number = {}
total_pc_numbers = []

for _ in range((3 ** number_of_matches) ** 2):
    pc_numbers = []
    for _ in range(number_of_matches):
        random_number = random.randint(1, 3)
        if random_number == 1:
            pc_numbers.append("1")
        elif random_number == 2:
            pc_numbers.append("2")
        else:
            pc_numbers.append("x")
    if pc_numbers not in total_pc_numbers:
        total_pc_numbers.append(pc_numbers)
    if len(total_pc_numbers) == min((3 ** number_of_matches), 20_000):
        break

total_find_number = []

for el in total_pc_numbers:
    find_number = 0
    for i in range(len(el)):
        if player_numbers[i] == el[i]:
            find_number += 1
    total_find_number.append(find_number)
print()

for el in total_find_number:
    if el not in dictionary_total_find_number:
        dictionary_total_find_number[el] = 1
    else:
        dictionary_total_find_number[el] += 1

sorted_dictionary = dict(sorted(dictionary_total_find_number.items(), key=lambda kv: (-kv[0], -kv[1])))

for (key, value) in sorted_dictionary.items():
    sum_values = sum(sorted_dictionary.values())
    print(f"Total: {key} -> Times: {value:_} -> {(value / sum_values * 100):.2f} %")
print()
res = sum(sorted_dictionary.values()) / (3 ** number_of_matches) * 100
print(f"{sum(sorted_dictionary.values()):_}")
print(f"{3 ** number_of_matches:_}")
print(f"{res:.2f} %")
