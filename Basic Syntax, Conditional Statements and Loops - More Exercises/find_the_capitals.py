text = input()

result = []
for ch in range(len(text)):
    if text[ch].isupper():
        result.append(ch)

print(result)
