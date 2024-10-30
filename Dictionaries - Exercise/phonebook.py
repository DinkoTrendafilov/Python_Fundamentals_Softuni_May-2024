phonebook = {}

while True:
    command = input()
    if "-" not in command:
        break
    split_command = command.split("-")
    name = split_command[0]
    number = split_command[1]
    phonebook[name] = number

searched = int(command)

for search in range(searched):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")


