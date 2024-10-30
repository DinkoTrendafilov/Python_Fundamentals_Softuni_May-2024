items = {
    "shards": 0,
    "fragments": 0,
    "motes": 0

}
is_legendary_item = False

while not is_legendary_item:
    current_items = input().split()

    for item in range(0, len(current_items), 2):
        key = current_items[item + 1].lower()
        value = int(current_items[item])

        if key in items:
            items[key] += value
        else:
            items[key] = value

        if items["shards"] >= 250:
            items["shards"] -= 250
            print("Shadowmourne obtained!")
            is_legendary_item = True

        if items["fragments"] >= 250:
            items["fragments"] -= 250
            print("Valanyr obtained!")
            is_legendary_item = True

        if items["motes"] >= 250:
            items["motes"] -= 250
            print("Dragonwrath obtained!")
            is_legendary_item = True

        if is_legendary_item:
            break

for material, quantity in items.items():
    print(f"{material}: {quantity}")
