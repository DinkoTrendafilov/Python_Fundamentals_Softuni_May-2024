def factorial_two_numbers(num1, num2):
    fact_res_1 = 1
    fact_res_2 = 1

    for i in range(1, num1 + 1):
        fact_res_1 *= i
    for i in range(1, num2 + 1):
        fact_res_2 *= i

    factorial_result = fact_res_1 / fact_res_2
    final_result = f"{factorial_result:.2f}"
    return final_result


first_number = int(input())
second_number = int(input())

result = factorial_two_numbers(first_number, second_number)
print(result)
