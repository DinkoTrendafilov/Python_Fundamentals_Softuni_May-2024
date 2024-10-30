def even_numbers(numbers: list) -> list:
    even_numbers_list = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers_list.append(num)
    return even_numbers_list


list_numbers = [int(num) for num in input().split()]
result = even_numbers(list_numbers)
print(result)
