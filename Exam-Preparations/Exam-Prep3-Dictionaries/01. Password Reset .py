password = input()

while True:
    command = input()
    if command == "Done":
        break

    split_command = command.split()
    action = split_command[0]

    if action == "TakeOdd":
        password = password[1::2]
        print(password)

    elif action == "Cut":
        index = int(split_command[1])
        length = int(split_command[2])
        substring = password[index:index + length]
        password = password.replace(substring, "", 1)
        print(password)

    elif action == "Substitute":
        substring = split_command[1]
        substitute = split_command[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
