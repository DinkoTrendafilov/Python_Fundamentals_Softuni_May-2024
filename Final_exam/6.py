numbers = [int(num) for num in input("Enter your  numbers: ").split()]

dictionary_numbers = {}
for num in numbers:
    if num not in dictionary_numbers:
        dictionary_numbers[num] = 1
    else:
        dictionary_numbers[num] += 1

sorted_dictionary = dict(sorted(dictionary_numbers.items(), key=lambda kv: (-kv[1], kv[0])))

total_diff = 0
counter = 0
total_sum_top_ten_value = 0
top_ten_count = sum(sorted_dictionary.values()) // 10
for (key, value) in sorted_dictionary.items():
    counter += 1
    if counter in range(1, top_ten_count + 1):
        total_sum_top_ten_value += value
    diff = value / sum(sorted_dictionary.values()) * 100
    total_diff += diff
    print(f"Number: {key} -->  {value} times  --> {diff:.2f} %")

print(f"{total_diff:.2f}")
print(
    f"Top 10 % numbers are: Count: {top_ten_count}: Value: {total_sum_top_ten_value} / {sum(sorted_dictionary.values())} "
    f"--> {(total_sum_top_ten_value / sum(sorted_dictionary.values()) * 100):.2f} %")
