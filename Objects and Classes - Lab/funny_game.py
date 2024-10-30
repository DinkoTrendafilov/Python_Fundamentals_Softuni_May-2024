import random

while True:
    number_of_iteration = int(input("Enter your number of iterations: "))
    count_of_numbers = int(input("Enter your range from 1 to end numbers: "))

    keys_dictionary = [num for num in range(1, count_of_numbers + 1)]
    values_dictionary = [0 for num in range(1, count_of_numbers + 1)]
    dictionary = dict(zip(keys_dictionary, values_dictionary))

    max_key = 0
    min_key = 0
    max_value = -float("inf")
    min_value = float("inf")

    for _ in range(number_of_iteration):
        numbers = []

        random_number = random.randint(1, count_of_numbers)
        numbers.append(random_number)

        for number in numbers:
            if number not in dictionary:
                dictionary[number] = 1
            else:
                dictionary[number] += 1

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

    print()
    for key, value in sorted_dictionary.items():
        print(f"Number: {key:02d} -> Value: {value:02d}")

        if value > max_value:
            max_key = key
            max_value = value
        if value < min_value:
            min_key = key
            min_value = value

    result = max_value / min_value * 100 - 100 if min_value != 0 else 0
    print()
    print(
        f"Different between Number: {max_key} --> {max_value} "
        f"times and Number {min_key} --> {min_value} times  =  {result:.2f}%")
    print()
