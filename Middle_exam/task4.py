targets = [int(num) for num in input().split()]

while True:
    command = input()
    if command == "End":
        break
    split_command = command.split()
    action = split_command[0]

    if action == "Shoot":
        index = int(split_command[1])
        power = int(split_command[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        index = int(split_command[1])
        value = int(split_command[2])

        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        index = int(split_command[1])
        radius = int(split_command[2])

        start_index = index - radius
        end_index = index + radius

        if start_index >= 0 and end_index < len(targets):
            del targets[start_index:end_index + 1]
        else:
            print("Strike missed!")

print("|".join(map(str, targets)))
