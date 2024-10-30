def min_max_sum(numbers: list):
    min_number = min(numbers)
    max_number = max(numbers)
    sum_numbers = sum(numbers)

    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_numbers}")


list_numbers = [int(num) for num in input().split()]
min_max_sum(list_numbers)
