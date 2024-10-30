targets = [int(number) for number in input().split()]

counter = 0

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index not in range(len(targets)):
        continue
    current_value = targets[index]
    if current_value == -1:
        continue
    targets[index] = -1
    counter += 1

    for current_index in range(len(targets)):
        if targets[current_index] == -1:
            continue
        if targets[current_index] > current_value:
            targets[current_index] -= current_value
        else:
            targets[current_index] += current_value

print(f"Shot targets: {counter} -> {' '.join([str(number) for number in targets])}")
