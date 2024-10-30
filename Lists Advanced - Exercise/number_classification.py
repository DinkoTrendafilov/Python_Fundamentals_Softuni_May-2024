numbers = [int(num) for num in input().split(", ")]

positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    else:
        negative_numbers.append(num)
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

positive_numbers_as_string = ", ".join(str(num) for num in positive_numbers)
negative_numbers_as_string = ", ".join(str(num) for num in negative_numbers)
even_numbers_as_string = ", ".join(str(num) for num in even_numbers)
odd_numbers_as_string = ", ".join(str(num) for num in odd_numbers)

print(f"Positive: {positive_numbers_as_string}")
print(f"Negative: {negative_numbers_as_string}")
print(f"Even: {even_numbers_as_string}")
print(f"Odd: {odd_numbers_as_string}")
