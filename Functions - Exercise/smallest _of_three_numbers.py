def smallest(numbers: list) -> list:
    smallest_number = min(numbers)
    return smallest_number


list_numbers = []
for num in range(3):
    current_number = int(input())
    list_numbers.append(current_number)

result = smallest(list_numbers)
print(result)
