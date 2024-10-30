import re

pattern = re.compile(r'>>(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)')

furniture_list = []
total_cost = 0

while True:
    line = input()
    if line == "Purchase":
        break

    match = pattern.match(line)
    if match:
        name = match.group('name')
        price = float(match.group('price'))
        quantity = int(match.group('quantity'))

        furniture_list.append(name)
        total_cost += price * quantity

print("Bought furniture:")
for furniture in furniture_list:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
