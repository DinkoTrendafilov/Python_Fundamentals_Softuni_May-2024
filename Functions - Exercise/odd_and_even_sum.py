def odd_and_even_sum(int_number: int):
    str_number = str(int_number)
    odd_sum = 0
    even_sum = 0
    for ch in str_number:
        if int(ch) % 2 == 0:
            even_sum += int(ch)
        else:
            odd_sum += int(ch)

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = int(input())
odd_and_even_sum(number)
