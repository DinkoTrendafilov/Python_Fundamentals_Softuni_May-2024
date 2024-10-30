import re

text = input()
while text:
    pattern = r"\d+"

    matches = re.findall(pattern, text)

    for match in matches:
        print(match, end=" ")
    text = input()


