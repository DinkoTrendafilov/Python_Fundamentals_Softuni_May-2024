def repeat_string(text, repeat_count):
    result = text * repeat_count
    return result


string_input = input()
repeat_number = int(input())

result_func = repeat_string(string_input, repeat_number)

print(result_func)
