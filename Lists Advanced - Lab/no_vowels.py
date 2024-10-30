text = input()
my_text_result = []

for ch in text:
    if ch.lower() not in ('a', 'o', 'u', 'e', 'i'):
        my_text_result.append(ch)

# print(*my_text_result, sep='')
print(''.join(my_text_result))
