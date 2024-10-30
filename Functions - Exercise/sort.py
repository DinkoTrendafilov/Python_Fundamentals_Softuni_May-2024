def sort_numbers(numbers: list) -> list:
    sorted_list = sorted(numbers)
    return sorted_list


int_numbers = [int(num) for num in input().split()]
result = sort_numbers(int_numbers)
print(result)
