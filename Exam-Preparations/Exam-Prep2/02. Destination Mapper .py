import re

text = input()
pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, text)

destinations = [match[1] for match in matches]
sum_result = sum([len(el) for el in destinations])

output = ", ".join(destinations)
print(f"Destinations: {output}")
print(f"Travel Points: {sum_result}")

