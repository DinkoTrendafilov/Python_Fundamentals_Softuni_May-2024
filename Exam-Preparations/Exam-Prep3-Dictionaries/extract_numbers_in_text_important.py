text = input()

number_as_string = ""
numbers = []

for i in range(len(text)):
    if i == len(text) - 1 and text[i].isdigit():
        number_as_string += text[i]
        numbers.append(number_as_string)

    if text[i].isdigit():
        number_as_string += text[i]
    else:
        if number_as_string != "":
            numbers.append(number_as_string)

        number_as_string = ""

numbers = [int(el) for el in numbers]
res = 1
for num in numbers:
    res *= num
print(*numbers)
print(f"Result of multiply numbers in list are: {res:,}")
