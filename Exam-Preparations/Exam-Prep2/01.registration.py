name = input()

while True:
    command = input()
    if command == "Registration":
        break
    split_command = command.split()
    action = split_command[0]

    if action == "Letters":
        lower_or_upper = split_command[1]
        if lower_or_upper == "Lower":
            name = name.lower()
        elif lower_or_upper == "Upper":
            name = name.upper()
        print(name)

    elif action == "Reverse":
        start_index = int(split_command[1])
        end_index = int(split_command[2])

        if start_index >= 0 and end_index < len(name):
            reversed_substring = name[start_index:end_index + 1][::-1]
            print(reversed_substring)

    elif action == "Substring":
        substring = split_command[1]

        if substring in name:
            res = name.replace(substring, "")
            print(res)
        else:
            print(f"The username {name} doesn't contain {substring}.")

    elif action == "Replace":
        char = split_command[1]

        name = name.replace(char, "-")
        print(name)

    elif action == "IsValid":
        char = split_command[1]

        if char in name:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")
