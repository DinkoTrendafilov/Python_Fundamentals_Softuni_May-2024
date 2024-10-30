my_list = [1, 2, 4, 2, 1, 8, 7, 3, 56, 12, 2, 5, 6, 4, 8, 9, 1, 1, 1, 2, 5, 11]

magic_number = 2

for index in range(len(my_list)):
    if my_list[index] == magic_number:
        print(f"Indexes of {magic_number} are: {index}")
