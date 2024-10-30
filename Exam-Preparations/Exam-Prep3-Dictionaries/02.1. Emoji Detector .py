import re

text = input()
pattern_num = r"\d"
res = re.findall(pattern_num, text)
numbers = [int(el) for el in res]

cool_threshold = 1

for num in numbers:
    cool_threshold *= num

pattern = r"(\:\:|\*\*)([A-Z][a-z]{2,})\1"

result = re.finditer(pattern, text)
cool_emojis = []
emojis_count = 0

for match in result:
    emojis_count += 1
    emoji = match.group()
    clear_emoji = match.group(2)

    emoji_coolness = sum([ord(el) for el in clear_emoji])

    if emoji_coolness >= cool_threshold:
        cool_emojis.append(emoji)

print()
print(f"Cool threshold: {cool_threshold}")
print(f"{emojis_count} emojis found in the text. The cool ones are:")

for el in cool_emojis:
    print(el)
