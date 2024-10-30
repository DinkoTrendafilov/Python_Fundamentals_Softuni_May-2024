text = input("Enter your text here: ")
text = text.replace(" ", "")

dictionary = {}
sum_text_ascii = sum([ord(char) for char in text])
sum_text_ascii = "{:,}".format(sum_text_ascii).replace(",", "_")

for char in text:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

dictionary = dict(sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0])))

for key, value in dictionary.items():
    print(f"Symbol: {key} -> Times: {value}")

print()
print(f"Total sum of ascii table is: {sum_text_ascii}")
