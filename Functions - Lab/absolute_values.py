def abs_numbers_list(numbers_list):
    abs_list_numbers = []
    for num in numbers_list:
        result = abs(num)
        abs_list_numbers.append(result)
    return abs_list_numbers


numbers = [float(num) for num in input().split()]

result_func = abs_numbers_list(numbers)
print(result_func)
