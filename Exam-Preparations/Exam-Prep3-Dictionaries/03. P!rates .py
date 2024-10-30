cities = {}

while True:
    data = input()
    if data == "Sail":
        break

    data_parts = data.split("||")
    city = data_parts[0]
    population = int(data_parts[1])
    gold = int(data_parts[2])

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

while True:
    event = input()
    if event == "End":
        break

    event_parts = event.split("=>")
    command = event_parts[0]
    town = event_parts[1]

    if command == "Plunder":
        people = int(event_parts[2])
        gold = int(event_parts[3])

        cities[town]["population"] -= people
        cities[town]["gold"] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[town]["population"] <= 0 or cities[town]["gold"] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        gold = int(event_parts[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, info in cities.items():
        print(f'{town} -> Population: {info["population"]} citizens, Gold: {info["gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
