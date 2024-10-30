number_of_electrons = int(input())

shells = []
for n in range(1, number_of_electrons + 1):
    result = 2 * n ** 2
    if number_of_electrons > result:
        shells.append(result)
        number_of_electrons -= result
    else:
        shells.append(number_of_electrons)
        break
print(shells)
