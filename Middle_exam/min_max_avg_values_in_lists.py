numbers = [int(num) for num in input().split()]
print()


for index, value in enumerate(numbers):
    print(f"Room: {index:02d}  =>  Value: {value:02d}")

avg = sum(numbers) / len(numbers)
closest_value = min(numbers, key=lambda x: abs(x - avg))
closest_index = numbers.index(closest_value)
diff = abs(closest_value - avg)

print()
print(f"Sum value in rooms = {sum(numbers)}")
print(f"Max value in rooms = {max(numbers)} at Index {numbers.index(max(numbers))}")
print(f"Min value in rooms = {min(numbers)} at Index {numbers.index(min(numbers))}")
print()
print(f"Average value in rooms = {avg:.2f}")
print(f"Average value: {closest_value} at Index = {closest_index} with difference: {diff:.2f} ")
