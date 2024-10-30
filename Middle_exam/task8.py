initial_loot = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break

    split_command = command.split()
    action = split_command[0]

    if action == "Loot":
        items = split_command[1:]
        for el in items:
            if el not in initial_loot:
                initial_loot.insert(0, el)

    elif action == "Drop":
        index = int(split_command[1])
        if index in range(len(initial_loot)):
            value = initial_loot[index]
            initial_loot.remove(value)
            initial_loot.append(value)

    elif action == "Steal":
        stolen_count = int(split_command[1])

        if stolen_count >= len(initial_loot):
            stolen_elements = initial_loot[::]
            print(*stolen_elements, sep=", ")
        else:
            stolen_elements = initial_loot[-stolen_count:]
            print(*stolen_elements, sep=", ")

        del initial_loot[-stolen_count:]

sum_initial_loot = [sum(len(el) for el in initial_loot)]
sum_initial_loot = sum_initial_loot[0]
len_initial_loot = len(initial_loot)


if initial_loot:
    avg_treasure_gain = sum_initial_loot / len_initial_loot
else:
    avg_treasure_gain = 0


if not initial_loot:
    print("Failed treasure hunt.")
else:
    print(f"Average treasure gain: {avg_treasure_gain:.2f} pirate credits.")
