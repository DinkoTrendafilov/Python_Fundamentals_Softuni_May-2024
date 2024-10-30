def add_and_subtract(num1: int, num2: int, num3: int) -> int:
    result = num1 + num2 - num3
    return result


number_one = int(input())
number_two = int(input())
number_three = int(input())

result_func = add_and_subtract(number_one, number_two, number_three)
print(result_func)
