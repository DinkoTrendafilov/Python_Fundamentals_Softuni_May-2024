numbers = [int(num) for num in input().split()]

middle = len(numbers) // 2

left_part = numbers[:middle]
right_part = numbers[middle:]

left_part_sum = 0
right_part_sum = 0

winner_part = ""
result = 0
for number in left_part:
    result += number
    if number == 0:
        result *= 0.8
left_part_sum += result

result1 = 0
for number in right_part:
    result1 += number
    if number == 0:
        result1 *= 0.8
right_part_sum += result1

if left_part_sum < right_part_sum:
    winner_part = "left"
else:
    winner_part = "right"

min_time = min(left_part_sum, right_part_sum)

print(f"The winner is {winner_part} with total time: {min_time:.1f}")
