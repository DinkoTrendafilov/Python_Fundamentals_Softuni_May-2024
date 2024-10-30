dictionary = {}

while True:
    command = input()
    if command == "stop":
        break
    item = command
    quantity = int(input())

    if item not in dictionary:
        dictionary[item] = quantity
    else:
        dictionary[item] += quantity

for item, values in dictionary.items():
    print(f"{item} -> {values}")
