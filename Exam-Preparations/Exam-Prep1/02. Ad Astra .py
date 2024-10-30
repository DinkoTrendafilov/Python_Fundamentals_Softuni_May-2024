import re

text = input()
pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"

matches = re.findall(pattern, text)

total_calories = sum([int(match[3]) for match in matches])
days = total_calories // 2_000

print(f"You have food to last you for: {days} days!")
for match in matches:
    items = match[1]
    exr_date = match[2]
    calories = match[3]
    print(f"Item: {items}, Best before: {exr_date}, Nutrition: {calories}")
