activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    split_command = command.split(">>>")
    action = split_command[0]

    if action == "Contains":
        substring = split_command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        upper_lower = split_command[1]
        start_index = int(split_command[2])
        end_index = int(split_command[3])

        if upper_lower == "Lower":
            changed_key = activation_key[start_index:end_index].lower()
            activation_key = activation_key[:start_index] + changed_key + activation_key[end_index:]
        elif upper_lower == "Upper":
            changed_key = activation_key[start_index:end_index].upper()
            activation_key = activation_key[:start_index] + changed_key + activation_key[end_index:]

        print(activation_key)

    elif action == "Slice":
        start_index = int(split_command[1])
        end_index = int(split_command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")
