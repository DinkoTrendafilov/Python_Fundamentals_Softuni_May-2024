first_number = int(input())
second_number = int(input())

max_number = 0

for i in range(second_number, first_number - 1, -1):
    if i % first_number == 0:
        max_number = i
        break

print(max_number)
