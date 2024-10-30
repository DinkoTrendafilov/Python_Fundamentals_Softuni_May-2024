numbers = [int(num) for num in input().split()]
count = int(input())


for _ in range(count):
    min_number = min(numbers)
    numbers.remove(min_number)


print(*numbers, sep=", ")

