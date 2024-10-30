number_of_elements_in_my_list = int(input())
my_list = [0] * number_of_elements_in_my_list

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if command[0] == 'add':
        people = int(command[1])
        my_list[-1] += people
    elif command[0] == 'insert':
        position = int(command[1])
        people = int(command[2])
        my_list[position] += people
    elif command[0] == 'leave':
        position = int(command[1])
        people = int(command[2])
        my_list[position] -= people

print(my_list)
