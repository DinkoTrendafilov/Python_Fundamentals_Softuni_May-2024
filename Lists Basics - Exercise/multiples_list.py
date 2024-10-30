multiples = int(input())
count = int(input())

number = [num * multiples for num in range(1, count + 1)]

print(number)
