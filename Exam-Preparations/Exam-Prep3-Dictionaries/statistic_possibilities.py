import random

number_of_iterations = int(input("Enter number of iterations: "))
dictionary = {}
total_result = []
total_0_1 = 0

for _ in range(number_of_iterations):
    result = []
    for _ in range(30):
        randon_number = random.randint(1, 100)
        if randon_number in range(1, 98):
            result.append(0)
        else:
            result.append(1)

    total_result.append(sum(result))

for num in total_result:
    if num not in dictionary:
        dictionary[num] = 1
    else:
        dictionary[num] += 1

print(f"{max(total_result):_}")
print(f"{min(total_result):_}")
print(f"{sum(total_result):_} --> {((sum(total_result) / number_of_iterations) * 100):.2f} %")

print()
sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))
for (key, value) in sorted_dictionary.items():
    if key in (0, 1):
        total_0_1 += value * 100 / number_of_iterations
    print(f"Sum: {key:02d} --> Times: {value:_} --> {((value / number_of_iterations) * 100):.2f} %")
print()
print(f"Total (0 + 1) count : {total_0_1:.2f} %")
