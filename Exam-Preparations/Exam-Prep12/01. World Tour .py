text = input()

while True:
    command = input()
    if command == "Travel":
        break
    split_command = command.split(":")
    action = split_command[0]

    if action == "Add Stop":
        index = int(split_command[1])
        string = split_command[2]

        if index in range(len(text)):
            text = text[:index] + string + text[index:]
        print(text)

    elif action == "Remove Stop":
        start_index = int(split_command[1])
        end_index = int(split_command[2])

        if start_index in range(len(text)) and end_index in range(len(text)):
            text = text[:start_index] + text[end_index + 1:]
        print(text)

    elif action == "Switch":
        old_string = split_command[1]
        new_string = split_command[2]

        if old_string in text:
            text = text.replace(old_string, new_string)
        print(text)

print(f"Ready for world tour! Planned stops: {text}")
