message = input()

while True:
    command = input()
    if command == "Reveal":
        break
    split_command = command.split(":|:")
    action = split_command[0]

    if action == "InsertSpace":
        index = int(split_command[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif action == "Reverse":
        substring = split_command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = split_command[1]
        replacement = split_command[2]
        message = message.replace(substring, replacement)
        print(message)

print(f"You have a new text message: {message}")
