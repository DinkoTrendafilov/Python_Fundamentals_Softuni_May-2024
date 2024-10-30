pirate_ship = [int(num) for num in input().split(">")]
warship = [int(num) for num in input().split(">")]
max_health = int(input())
is_win = False

while True:
    command = input()
    if command == "Retire":
        break
    split_command = command.split()
    action = split_command[0]

    if action == "Fire":
        index = int(split_command[1])
        damage = int(split_command[2])
        if index in range(len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                warship.pop(index)
                print("You won! The enemy ship has sunken.")
                is_win = True
                break

    elif action == "Defend":
        start_index = int(split_command[1])
        end_index = int(split_command[2])
        damage = int(split_command[3])
        if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_win = True
                    break

    elif action == "Repair":
        index = int(split_command[1])
        health = int(split_command[2])
        if index in range(len(pirate_ship)):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif action == "Status":
        count = 0
        for el in pirate_ship:
            if el < max_health * 0.2:
                count += 1

        print(f"{count} sections need repair.")

pirate_ship_sum = sum(pirate_ship)
warship_sum = sum(warship)

if not is_win:
    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {warship_sum}")
