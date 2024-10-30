import re

text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

matches = re.findall(pattern, text)
words = []
count_of_matches = len(list(matches))

for match in matches:
    word = str(match[1])
    rev_word = str(match[2])

    if word == rev_word[::-1]:
        words.append(word)
        words.append(rev_word)

if count_of_matches == 0:
    print("No word pairs found!")
else:
    print(f"{count_of_matches} word pairs found!")

if len(words) != 0:
    print("The mirror words are:")
    for i in range(0, len(words), 2):
        word = words[i]
        rev_word = words[i + 1]
        if i == len(words) - 2 and i + 1 == len(words) - 1:
            print(f"{word} <=> {rev_word}")
        else:
            print(f"{word} <=> {rev_word}", end=", ")

else:
    print("No mirror words!")
