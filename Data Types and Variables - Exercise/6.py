numbers = [14, 29, 1, 7, 19, 41, 27, 91, 4, -1, -19, -34, -32, -11, 17, 22, 33]

sum_list = sum(numbers)
len_list = len(numbers)
avg_list = sum_list / len_list

favorite_numbers = [num for num in numbers if 10 <= num <= 20]

print(*numbers)
print(sum_list)
print(len_list)
print(avg_list)
print()
print(*favorite_numbers)

