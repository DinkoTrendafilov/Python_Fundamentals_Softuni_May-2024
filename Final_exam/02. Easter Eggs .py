import re

text = input()

pattern = r"[@#]+([a-z]{3,})[@#]+[^a-zA-Z0-9]*\/(\d+)\/"

matches = re.findall(pattern, text)

for match in matches:
    color = match[0]
    amount = match[1]
    print(f"You found {amount} {color} eggs!")
