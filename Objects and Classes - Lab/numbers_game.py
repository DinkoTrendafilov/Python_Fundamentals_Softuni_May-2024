import random

while True:
    number_of_iteration = int(input("Enter number of iterations: "))

    numbers = []

    keys = [x for x in range(1, 51)]
    values = [0 for x in range(1, 51)]
    dictionary = dict(zip(keys, values))

    for _ in range(number_of_iteration):
        random_number = random.randint(0, 50)
        numbers.append(random_number)

    for num in numbers:
        if num not in dictionary:
            dictionary[num] = 1
        else:
            dictionary[num] += 1

    dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

    for key, value in dictionary.items():
        print(f"Number: {key:02d} -> Value: {value:02d}")

    avg_numbers = sum(numbers) / len(numbers)
    avg = 25
    result = ((avg_numbers / avg) * 100) - 100 if number_of_iteration >= 10 else 0
    print()
    print(f"Average value is: {avg_numbers:.2f} to {avg:.2f}  -----  {result:.2f} % deviation")

