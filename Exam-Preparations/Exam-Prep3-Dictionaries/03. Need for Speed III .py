number_of_cards = int(input())

cars_info = {}

for _ in range(number_of_cards):
    data = input().split("|")
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    if car not in cars_info:
        cars_info[car] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input()
    if command == "Stop":
        break

    split_command = command.split(" : ")
    action = split_command[0]
    car = split_command[1]

    if action == "Drive":
        distance = int(split_command[2])
        fuel_needed = int(split_command[3])

        if cars_info[car]["fuel"] < fuel_needed:
            print("Not enough fuel to make that ride")
            continue
        else:
            cars_info[car]["mileage"] += distance
            cars_info[car]["fuel"] -= fuel_needed
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")

            if cars_info[car]["mileage"] >= 100_000:
                print(f"Time to sell the {car}!")
                del cars_info[car]

    elif action == "Refuel":
        fuel_added = int(split_command[2])

        if cars_info[car]["fuel"] + fuel_added > 75:
            fuel_added = 75 - cars_info[car]["fuel"]
        cars_info[car]["fuel"] += fuel_added
        print(f"{car} refueled with {fuel_added} liters")

    elif action == "Revert":
        kilometers = int(split_command[2])

        if cars_info[car]["mileage"] - kilometers < 10_000:
            cars_info[car]["mileage"] = 10_000
        else:
            cars_info[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in cars_info.items():
    print(f'{key} -> Mileage: {value["mileage"]} kms, Fuel in the tank: {value["fuel"]} lt.')
