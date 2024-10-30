number_of_halls = int(input())
free_chairs = 0
flag = False
free_chairs = 0

for hall in range(1, number_of_halls + 1):
    command = input().split()
    chairs = command[0]
    number_of_visitors = int(command[1])
    diff = abs(len(chairs) - number_of_visitors)
    if len(chairs) < number_of_visitors:
        print(f"{diff} more chairs needed in room {hall}")
        flag = True
    else:
        free_chairs += diff

if not flag:
    print(f"Game On, {free_chairs} free chairs left")

