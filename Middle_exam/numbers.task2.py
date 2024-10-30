numbers = [int(num) for num in input().split()]

while True:
    command = input()
    if command == "Finish":
        break
    split_command = command.split()
    action = split_command[0]

    if action == "Remove":
        value = int(split_command[1])
        numbers.remove(value)

    elif action == "Add":
        value = int(split_command[1])
        numbers.append(value)

    elif action == "Replace":
        value = int(split_command[1])
        replacement = int(split_command[2])
        if value in numbers:
            index_value = numbers.index(value)
            numbers[index_value] = replacement

    elif action == "Collapse":
        value = int(split_command[1])
        numbers = [num for num in numbers if num >= value]

print(" ".join(map(str, numbers)))
