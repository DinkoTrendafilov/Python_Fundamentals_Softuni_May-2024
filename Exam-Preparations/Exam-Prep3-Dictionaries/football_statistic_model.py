import random

n = int(input("Enter number of iterations: "))
result = []
dictionary = {}
one_counter, best_one, without_one, best_without_one = 0, 0, 0, 0
two_counter, best_two, without_two, best_without_two = 0, 0, 0, 0
draw_counter, best_draw, without_draw, best_without_draw = 0, 0, 0, 0
balanced_group = 0
zeros_group = 0
total_groups = n // 15
best_without_0_in_row = 0
counter_without_0 = 0

for _ in range(n):
    random_number = random.randint(1, 3)
    if random_number == 1:
        result.append("1")
    elif random_number == 2:
        result.append("2")
    else:
        result.append("X")

for el in result:
    if el == "1":
        if without_one > best_without_one:
            best_without_one = without_one
        without_one = 0
        without_draw += 1
        without_two += 1
        one_counter += 1
        two_counter = 0
        draw_counter = 0
        if one_counter > best_one:
            best_one = one_counter

    elif el == "2":
        if without_two > best_without_two:
            best_without_two = without_two
        without_two = 0
        without_draw += 1
        without_one += 1
        two_counter += 1
        one_counter = 0
        draw_counter = 0
        if two_counter > best_two:
            best_two = two_counter

    else:
        if without_draw > best_without_draw:
            best_without_draw = without_draw
        without_draw = 0
        without_two += 1
        without_one += 1
        draw_counter += 1
        one_counter = 0
        two_counter = 0
        if draw_counter > best_draw:
            best_draw = draw_counter

for el in result:
    if el not in dictionary:
        dictionary[el] = 1
    else:
        dictionary[el] += 1

for i in range(0, len(result), 15):
    sub_result = result[i:i + 15]
    if 6 >= sub_result.count("1") >= 4 and 6 >= sub_result.count("2") >= 4 and 6 >= sub_result.count("X") >= 4:
        balanced_group += 1
    if sub_result.count("1") == 0 or sub_result.count("2") == 0 or sub_result.count("X") == 0:
        zeros_group += 1
        counter_without_0 = 0
    else:
        counter_without_0 += 1
        if counter_without_0 > best_without_0_in_row:
            best_without_0_in_row = counter_without_0

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

print()
for (key, value) in sorted_dictionary.items():
    print(f"Number {key} ---> Times: {value:_} ---> ({(value / n) * 100:.2f}%)")

print()
print(f"Best [1] in row: {best_one} --> Best [without 1] in row: {best_without_one}")
print(f"Best [X] in row: {best_draw} --> Best [without X] in row: {best_without_draw}")
print(f"Best [2] in row: {best_two} --> Best [without 2] in row: {best_without_two}")
print()
print(f"Balanced groups count: {balanced_group:_} ---> {((balanced_group / (n / 15)) * 100):.2f} %")
print(f"Zeros groups count: {zeros_group:_} ---> {((zeros_group / (n / 15)) * 100):.2f} %")
print()
print(f"Total groups: {total_groups:_}  --> the best result in row [without 0] --> {best_without_0_in_row:_}")
print()
