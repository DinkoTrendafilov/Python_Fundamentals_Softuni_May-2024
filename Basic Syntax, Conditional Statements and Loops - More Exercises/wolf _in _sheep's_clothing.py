list_animals = input().split(", ")


if list_animals[- 1] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    sheep_position = len(list_animals) - list_animals.index("wolf") - 1
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")


