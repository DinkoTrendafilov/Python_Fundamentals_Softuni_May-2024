text = input()

while True:
    command = input()
    if command == "Abracadabra":
        break
    split_command = command.split()
    action = split_command[0]

    if action == "Abjuration":
        text = text.upper()
        print(text)

    elif action == "Necromancy":
        text = text.lower()
        print(text)

    elif action == "Illusion":
        index = int(split_command[1])
        letter = split_command[2]

        if index not in range(len(text)):
            print("The spell was too weak.")
        else:
            text = text[:index] + letter + text[index + 1:]
            print("Done!")

    elif action == "Divination":
        first_substring = split_command[1]
        secons_substring = split_command[2]
        text = text.replace(first_substring, secons_substring)
        print(text)

    elif action == "Alteration":
        substring = split_command[1]
        text = text.replace(substring, "")
        print(text)
    else:
        print("The spell did not work!")
