import re

text = input()
word = input()

pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
matches = pattern.findall(text)

print(len(matches))
