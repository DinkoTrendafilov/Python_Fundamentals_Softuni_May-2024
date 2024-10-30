while True:
    names = ["Ivan", "Dimo", "Kosta", "Simeon", "Ivo", "Dinko"]
    ages = [23, 17, 21, 41, 24, 45]

    dictionary = dict(zip(names, ages))

    command = input("Enter name or information of full data as i: ")
    if command == "i":
        for key, value in dictionary.items():
            print(f"Name: {key} - Age: {value}")
            continue

    name = command

    dictionary = dict(zip(names, ages))

    if name in dictionary:
        print(f"Age of {name}: {dictionary[name]}")
    else:
        print("Name not found!")

    print()
