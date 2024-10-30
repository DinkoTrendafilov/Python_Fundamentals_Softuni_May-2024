def combination_calculator(num1, num2):
    numerator = 1
    for num in range(num2, (num2 - num1), -1):
        numerator *= num

    denumerator = 1
    for num in range(num1, 0, -1):
        denumerator *= num

    result = numerator // denumerator
    result = "{:,}".format(result).replace(",", "_")
    print(f"Общият брой комбинации на {first_number} от {second_number} = {result}")
    return result


first_number = int(input("Моля въведенете броя ма избраните елементи: "))
second_number = int(input("Моля въведенете общият брой елементи: "))

combination_calculator(first_number,second_number)
