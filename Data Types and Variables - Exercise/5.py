my_list = [1, 3, 2, 4, 6, 8, 9, 7]
print(*my_list)

my_list.insert(-1, 1_000)
print(*my_list)

my_list += [12, 13, 14, 15]
print(*my_list)
