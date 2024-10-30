def rounding_numbers(numbers_list):
    new_list_numbers = []
    for num in numbers_list:
        round_value = round(num)
        new_list_numbers.append(round_value)
    return new_list_numbers


numbers = [float(num) for num in input().split()]

result_func = rounding_numbers(numbers)
print(result_func)
