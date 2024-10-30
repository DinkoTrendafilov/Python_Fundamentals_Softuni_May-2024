import random

while True:
    number_of_iteration = int(input("Enter your number of iterations: "))
    numbers = []
    count_1 = 0
    best_1 = 0

    count_2 = 0
    best_2 = 0

    count_3 = 0
    best_3 = 0

    count_4 = 0
    best_4 = 0

    for iteration in range(1, number_of_iteration + 1):
        random_number = random.randint(1, 4)
        numbers.append(random_number)

    for number in numbers:
        if number == 1:
            count_1 += 1
            if count_1 > best_1:
                best_1 = count_1

            count_2 = 0
            count_3 = 0
            count_4 = 0

        elif number == 2:
            count_2 += 1
            if count_2 > best_2:
                best_2 = count_2

            count_1 = 0
            count_3 = 0
            count_4 = 0

        elif number == 3:
            count_3 += 1
            if count_3 > best_3:
                best_3 = count_3

            count_1 = 0
            count_2 = 0
            count_4 = 0

        elif number == 4:
            count_4 += 1
            if count_4 > best_4:
                best_4 = count_4

            count_1 = 0
            count_2 = 0
            count_3 = 0

    one_as_percent = round(numbers.count(1) / number_of_iteration * 100, 2)
    two_as_percent = round(numbers.count(2) / number_of_iteration * 100, 2)
    three_as_percent = round(numbers.count(3) / number_of_iteration * 100, 2)
    four_as_percent = round(100 - (one_as_percent + two_as_percent + three_as_percent), 2)

    print(f"Total count of 1 is: {(numbers.count(1))} times - {one_as_percent}% - Best 1 in row is: {best_1}")
    print(f"Total count of 2 is: {(numbers.count(2))} times - {two_as_percent}% - Best 2 in row is: {best_2}")
    print(f"Total count of 3 is: {(numbers.count(3))} times - {three_as_percent}% - Best 3 in row is: {best_3}")
    print(f"Total count of 4 is: {(numbers.count(4))} times - {four_as_percent}% - Best 4 in row is: {best_4}")
    print()

