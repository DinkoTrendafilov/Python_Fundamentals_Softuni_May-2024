text = input()
text = text.replace(" ", "")
dictionary = {}

for char in text:
    if char not in dictionary:
        dictionary[char] = 1
    else:
        dictionary[char] += 1


for key, value in dictionary.items():
    print(f"{key} -> {value}")

