parking = {}
number_of_clients = int(input())

for _ in range(number_of_clients):
    current_command = input().split()
    command = current_command[0]
    name = current_command[1]

    if command == "register":
        car_number = current_command[2]
        if name not in parking:
            parking[name] = car_number
            print(f"{name} registered {car_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_number}")

    elif command == "unregister":
        if name in parking:
            del parking[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, car_number in parking.items():
    print(f"{name} => {car_number}")



