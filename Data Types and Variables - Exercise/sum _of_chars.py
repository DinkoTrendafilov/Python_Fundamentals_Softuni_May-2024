number_of_lines = int(input())
total_sum = 0

for line in range(1, number_of_lines + 1):
    current_char = input()
    total_sum += ord(current_char)

print(f"The sum equals: {total_sum}")
