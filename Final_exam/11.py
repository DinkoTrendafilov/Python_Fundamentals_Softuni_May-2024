numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
    , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
    , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
    , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

dictionary = {}
total_result = []
current_result = 14
win_result = 0
lose_result = 0

for result in numbers:
    a = current_result + result
    total_result.append(a)

for el in total_result:
    if el not in dictionary:
        dictionary[el] = 1
    else:
        dictionary[el] += 1

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

for (key, value) in sorted_dictionary.items():
    if key in range(1, 22):
        win_result += value
    else:
        lose_result += value
    print(f"Result: {key} -> Times: {value:_}")

print()
print(f"Win result is: {win_result} --> {(win_result / (win_result + lose_result) * 100):.2f} %")
print(f"Lose result is: {lose_result} --> {(lose_result / (win_result + lose_result) * 100):.2f} %")
print(sum(sorted_dictionary.values()))
