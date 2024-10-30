message = input()

while True:
    command = input()
    if command == "Decode":
        break
    split_command = command.split("|")
    action = split_command[0]

    if action == "Move":
        number_of_letters = int(split_command[1])
        change_part = message[:number_of_letters]
        message = message[number_of_letters:] + change_part

    elif action == "Insert":
        index = int(split_command[1])
        value = split_command[2]
        message = message[:index] + value + message[index:]

    elif action == "ChangeAll":
        substring = split_command[1]
        replacement = split_command[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
