import random

n = int(input("Моля въведете броят на хвърлянията на монетата: "))
dictionary = {}
results = []
ezi_counter, tura_counter = 0, 0
best_ezi, best_tura = 0, 0

for _ in range(n):
    random_number = random.randint(1, 2)
    if random_number == 1:
        results.append("Ези")
        tura_counter = 0
        ezi_counter += 1
        if ezi_counter > best_ezi:
            best_ezi = ezi_counter
    else:
        ezi_counter = 0
        tura_counter += 1
        if tura_counter > best_tura:
            best_tura = tura_counter
        results.append("Тура")

for el in results:
    if el not in dictionary:
        dictionary[el] = 1
    else:
        dictionary[el] += 1

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

print(*results)
print()
max_value = max(sorted_dictionary.values())
min_value = min(sorted_dictionary.values())
diff = max_value / min_value * 100 - 100
for key, value in sorted_dictionary.items():
    print(f"{key} -> {value:_}")
print()
print(f"Best count of 'Ези': {best_ezi}")
print(f"Best count of 'Тура': {best_tura}")
print(f"Difference: {diff:.2f} %")
