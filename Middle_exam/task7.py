item_list = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    split_command = command.split(" - ")
    action = split_command[0]

    if action == "Collect":
        item = split_command[1]
        if item not in item_list:
            item_list.append(item)
    elif action == "Drop":
        item = split_command[1]
        if item in item_list:
            item_list.remove(item)
    elif action == "Combine Items":
        items = split_command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in item_list:
            index_old_item = item_list.index(old_item)
            item_list.insert(index_old_item + 1, new_item)
    elif action == "Renew":
        item = split_command[1]
        if item in item_list:
            item_list.remove(item)
            item_list.append(item)

print(*item_list, sep=", ")
