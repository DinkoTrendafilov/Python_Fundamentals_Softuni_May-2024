import random

while True:

    number_of_iteration = int(input("Enter your number of iterations: "))
    numbers = []
    count_0 = 0
    best_0 = 0

    count_1 = 0
    best_1 = 0

    for iteration in range(1, number_of_iteration + 1):
        random_number = random.randint(0, 1)
        numbers.append(random_number)

    for number in numbers:
        if number == 0:
            count_0 += 1
            if count_0 > best_0:
                best_0 = count_0

            count_1 = 0
        else:
            count_1 += 1
            if count_1 > best_1:
                best_1 = count_1
            count_0 = 0

    ezi_as_percent = round(numbers.count(0) / number_of_iteration * 100, 2)
    tura_as_percent = round(100 - ezi_as_percent, 2)
    print(f"Total count of ezi is: {(numbers.count(0))} - {ezi_as_percent}% - Best ezi in row is: {best_0}")
    print(f"Total count of tura is: {(numbers.count(1))} - {tura_as_percent}% - Best tura in row is: {best_1}")
    print()
