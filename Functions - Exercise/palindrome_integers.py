def palindrome_number(number: str) -> bool:
    if number == number[::-1]:
        return True
    return False


numbers_list = input().split(", ")

for num in numbers_list:
    result_funk = palindrome_number(num)
    print(result_funk)
