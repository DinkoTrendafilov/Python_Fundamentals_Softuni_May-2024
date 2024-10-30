import random

while True:
    number_of_iterations = int(input("Enter numbers of iteration: "))

    total_result = []
    in_row_1, best_row_1 = 0, 0
    in_row_2, best_row_2 = 0, 0
    in_row_3, best_row_3 = 0, 0
    in_row_4, best_row_4 = 0, 0
    in_row_5, best_row_5 = 0, 0
    in_row_6, best_row_6 = 0, 0
    in_row_7, best_row_7 = 0, 0
    in_row_8, best_row_8 = 0, 0
    in_row_9, best_row_9 = 0, 0
    in_row_10, best_row_10 = 0, 0

    for _ in range(number_of_iterations):
        number = random.randint(1, 10)
        total_result.append(number)

    for num in total_result:
        if num == 1:
            in_row_1 += 1
            in_row_2 = 0
            in_row_3 = 0
            in_row_4 = 0
            in_row_5 = 0
            in_row_6 = 0
            in_row_7 = 0
            in_row_8 = 0
            in_row_9 = 0
            in_row_10 = 0
            if in_row_1 > best_row_1:
                best_row_1 = in_row_1

        elif num == 2:
            in_row_1 = 0
            in_row_2 += 1
            in_row_3 = 0
            in_row_4 = 0
            in_row_5 = 0
            in_row_6 = 0
            in_row_7 = 0
            in_row_8 = 0
            in_row_9 = 0
            in_row_10 = 0
            if in_row_2 > best_row_2:
                best_row_2 = in_row_2
        elif num == 3:
            in_row_1 = 0
            in_row_2 = 0
            in_row_3 += 1
            in_row_4 = 0
            in_row_5 = 0
            in_row_6 = 0
            in_row_7 = 0
            in_row_8 = 0
            in_row_9 = 0
            in_row_10 = 0
            if in_row_3 > best_row_3:
                best_row_3 = in_row_3
        elif num == 4:
            in_row_1 = 0
            in_row_2 = 0
            in_row_3 = 0
            in_row_4 += 1
            in_row_5 = 0
            in_row_6 = 0
            in_row_7 = 0
            in_row_8 = 0
            in_row_9 = 0
            in_row_10 = 0
            if in_row_4 > best_row_4:
                best_row_4 = in_row_4
        elif num == 5:
            in_row_1 = 0
            in_row_2 = 0
            in_row_3 = 0
            in_row_4 = 0
            in_row_5 += 1
            in_row_6 = 0
            in_row_7 = 0
            in_row_8 = 0
            in_row_9 = 0
            in_row_10 = 0
            if in_row_5 > best_row_5:
                best_row_5 = in_row_5
        elif num == 6:
            in_row_1 = 0
            in_row_2 = 0
            in_row_3 = 0
            in_row_4 = 0
            in_row_5 = 0
            in_row_6 += 1
            in_row_7 = 0
            in_row_8 = 0
            in_row_9 = 0
            in_row_10 = 0
            if in_row_6 > best_row_6:
                best_row_6 = in_row_6
        elif num == 7:
            in_row_1 = 0
            in_row_2 = 0
            in_row_3 = 0
            in_row_4 = 0
            in_row_5 = 0
            in_row_6 = 0
            in_row_7 += 1
            in_row_8 = 0
            in_row_9 = 0
            in_row_10 = 0
            if in_row_7 > best_row_7:
                best_row_7 = in_row_7
        elif num == 8:
            in_row_1 = 0
            in_row_2 = 0
            in_row_3 = 0
            in_row_4 = 0
            in_row_5 = 0
            in_row_6 = 0
            in_row_7 = 0
            in_row_8 += 1
            in_row_9 = 0
            in_row_10 = 0
            if in_row_8 > best_row_8:
                best_row_8 = in_row_8
        elif num == 9:
            in_row_1 = 0
            in_row_2 = 0
            in_row_3 = 0
            in_row_4 = 0
            in_row_5 = 0
            in_row_6 = 0
            in_row_7 = 0
            in_row_8 = 0
            in_row_9 += 1
            in_row_10 = 0
            if in_row_9 > best_row_9:
                best_row_9 = in_row_9
        elif num == 10:
            in_row_1 = 0
            in_row_2 = 0
            in_row_3 = 0
            in_row_4 = 0
            in_row_5 = 0
            in_row_6 = 0
            in_row_7 = 0
            in_row_8 = 0
            in_row_9 = 0
            in_row_10 += 1
            if in_row_10 > best_row_10:
                best_row_10 = in_row_10

    print(f"The best in row of 1 is ==>  {best_row_1}")
    print(f"The best in row of 2 is ==>  {best_row_2}")
    print(f"The best in row of 3 is ==>  {best_row_3}")
    print(f"The best in row of 4 is ==>  {best_row_4}")
    print(f"The best in row of 5 is ==>  {best_row_5}")
    print(f"The best in row of 6 is ==>  {best_row_6}")
    print(f"The best in row of 7 is ==>  {best_row_7}")
    print(f"The best in row of 8 is ==>  {best_row_8}")
    print(f"The best in row of 9 is ==>  {best_row_9}")
    print(f"The best in row of 10 is ==>  {best_row_10}")
