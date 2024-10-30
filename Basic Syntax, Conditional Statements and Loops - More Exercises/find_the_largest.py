number = input()

list_number = [int(num) for num in number]
list_number = sorted(list_number)[::-1]

print(*list_number, sep="")
