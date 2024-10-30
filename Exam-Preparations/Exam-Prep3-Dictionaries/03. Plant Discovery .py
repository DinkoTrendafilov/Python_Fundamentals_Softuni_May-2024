n = int(input())

plants = {}

for _ in range(n):
    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])
    if plant in plants:
        plants[plant]['rarity'] = rarity
    else:
        plants[plant] = {'rarity': rarity, 'ratings': []}

while True:
    command = input()
    if command == "Exhibition":
        break

    command = command.split(": ")
    action = command[0]
    details = command[1].split(" - ")

    if action == "Rate":
        plant = details[0]
        rating = float(details[1])
        if plant in plants:
            plants[plant]['ratings'].append(rating)
        else:
            print("error")
    elif action == "Update":
        plant = details[0]
        new_rarity = int(details[1])
        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print("error")
    elif action == "Reset":
        plant = details[0]
        if plant in plants:
            plants[plant]['ratings'] = []
        else:
            print("error")

print("Plants for the exhibition:")
for plant, info in plants.items():
    average_rating = sum(info['ratings']) / len(info['ratings']) if info['ratings'] else 0
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average_rating:.2f}")
