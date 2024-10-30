number_of_people = int(input())
capacity = int(input())
result = 0

if number_of_people % capacity == 0:
    result = number_of_people / capacity
else:
    result = int(number_of_people / capacity) + 1

print(int(result))
