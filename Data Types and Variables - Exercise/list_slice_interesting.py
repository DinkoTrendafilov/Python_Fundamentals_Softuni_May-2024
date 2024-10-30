input_line = input().split()
my_list = [int(num) for num in input_line]

sorted_rev_list = sorted(my_list, reverse=True)
slice_result = my_list[::-2]  # start_point:end_point:step
filter_result = [num for num in my_list if num not in slice_result]

avg = sum(my_list) / len(my_list)

print(*sorted_rev_list)
print(*slice_result)
print(*filter_result)
print(avg)
print(len(str(avg)))
print(len(my_list))
