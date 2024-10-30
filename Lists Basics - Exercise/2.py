my_list = [-21, -12, 27, -9, 45, 26, -19, 43, -31, -17, -13, -11, 5, 6]

rev_sort_list = sorted(my_list, reverse=True)
avg = sum(my_list) / len(my_list)


print(*my_list)
print(*rev_sort_list)
print(sum(my_list))
print(len(my_list))
print(avg)

for index, value in enumerate(my_list):
    print(f"Index is: {index:02d}, Value is: {value:02d}")

