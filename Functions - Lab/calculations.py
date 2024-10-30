def calculator(num1, num2, operator):
    if operator == "multiply":
        result = num1 * num2
        return result
    elif operator == "divide":
        result = num1 // num2
        return result
    elif operator == "add":
        result = num1 + num2
        return result
    elif operator == "subtract":
        result = num1 - num2
        return result


input_operator = input()
first_number = int(input())
second_number = int(input())

result_func = calculator(first_number, second_number, input_operator)
print(result_func)
