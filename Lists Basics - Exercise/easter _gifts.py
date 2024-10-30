gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    split_command = command.split()
    action = split_command[0]
    if action == "OutOfStock":
        item = split_command[1]
        while item in gifts:
            index = gifts.index(item)
            gifts[index] = "None"
    elif action == "Required":
        item = split_command[1]
        index = int(split_command[2])
        if index in range(len(gifts)):
            gifts[index] = item
    elif action == "JustInCase":
        item = split_command[1]
        gifts[-1] = item

result = [item for item in gifts if item != "None"]
print(*result)
