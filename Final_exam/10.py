a = [num for num in range(52, 39, -1)]
b = [num for num in range(13, 0, -1)]

result_a = 1
result_b = 1

for el in a:
    result_a *= el

for el in b:
    result_b *= el

print(f"Total number of combination of bridge is: {int(result_a / result_b):_}")
