rooms = input().split("|")

initial_health = 100
initial_bitcoins = 0
is_death = False

for index, room in enumerate(rooms, start=1):
    split_room = room.split()
    command = split_room[0]
    number = int(split_room[1])

    if command == "potion":
        initial_health += number
        if initial_health >= 100:
            diff = abs(initial_health - 100)
            result = number - diff
            initial_health = 100
            print(f"You healed for {result} hp.")
            print(f"Current health: {initial_health} hp.")
        else:
            print(f"You healed for {number} hp.")
            print(f"Current health: {initial_health} hp.")

    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            is_death = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {index}")
            break

if not is_death:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
