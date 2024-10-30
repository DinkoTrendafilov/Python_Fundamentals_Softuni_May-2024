import random

while True:
    matches_count = int(input("Enter numbers count: "))
    iterations_count = int(input("Enter iteration count: "))
    needed_percent = int(input("Enter needed %: "))

    result_player = []
    dictionary = {}

    for iteration in range(iterations_count):
        random_number = random.randint(1, matches_count)
        result_player.append(random_number)

    for el in result_player:
        if el not in dictionary:
            dictionary[el] = 1
        else:
            dictionary[el] += 1

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

    print(f"{'-' * 100}")
    for (key, value) in sorted_dictionary.items():
        print(f"Result: {key} -> Times: {value:_} -> {(value / iterations_count * 100):.2f} %")

    print(f"{'-' * 100}")
    print("Results are: ")
    needed_number = int(len(sorted_dictionary) * needed_percent / 100)
    counter = 0
    total_value = 0
    for (key, value) in sorted_dictionary.items():
        counter += 1
        if counter in range(1, needed_number + 1):
            print(f"Key: {key} --> Value: {value:_}")
            total_value += value
    print(f"{'-' * 100}")
    print(f"Top: {needed_percent} %  makes: {((total_value / iterations_count) * 100):.2f} %")
    print(f"{'-' * 100}")
    print(f"Matches count: {matches_count:_}")
    print(f"Count of elements: {len(sorted_dictionary):_}")
    print(f"Needed %: {needed_percent}")
    print(f"Needed range numbers [1 - {needed_number:_}] -->  {needed_number:_}")
    print(f"{'-' * 100}")

    diff = max(sorted_dictionary.values()) / min(sorted_dictionary.values()) * 100 - 100 \
        if len(sorted_dictionary) > 1 and min(sorted_dictionary.values()) != max(sorted_dictionary.values()) else 0
    print(f"Difference between MAX: {max(sorted_dictionary.values()):_} and "
          f"MIN: {min(sorted_dictionary.values()):_} values: {diff:.2f} %")
    print(f"{'-' * 100}")