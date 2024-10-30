import re

text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

matches = re.findall(pattern, text)
mirror_words = []
count_of_matches = len(matches)

for match in matches:
    word = str(match[1])
    rev_word = str(match[2])

    if word == rev_word[::-1]:
        mirror_words.append(f"{word} <=> {rev_word}")

if count_of_matches == 0:
    print("No word pairs found!")
else:
    print(f"{count_of_matches} word pairs found!")

if len(mirror_words) != 0:
    print("The mirror words are:")
    print(*mirror_words, sep=", ")

else:
    print("No mirror words!")
