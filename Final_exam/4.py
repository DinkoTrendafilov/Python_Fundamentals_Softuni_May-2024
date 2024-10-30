import random

n = int(input("Enter number of iterations: "))
total_pc_numbers = []
good_try = 0
bad_try = 0
numbers = []
for num in range(n):
    pc_numbers = []
    for _ in range(13):
        random_number = random.randint(1, 3)
        if random_number == 1:
            pc_numbers.append("1")
        elif random_number == 2:
            pc_numbers.append("2")
        else:
            pc_numbers.append("x")

    if pc_numbers not in total_pc_numbers:
        total_pc_numbers.append(pc_numbers)
        good_try += 1
    else:
        bad_try += 1
        numbers.append(num)

print(f"Good tries: {good_try:_} -> {((good_try / (good_try + bad_try)) * 100):.2f} %")
print(f"Bad tries: {bad_try:_} -> {((bad_try / (good_try + bad_try)) * 100):.2f} % "
      f"--> {", ".join(str(el) for el in numbers)}")

