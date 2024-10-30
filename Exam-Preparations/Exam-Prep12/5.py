n = int(input())

heroes = {}
for _ in range(n):
    command = input().split()
    hero_name = command[0]
    hp = int(command[1])
    mp = int(command[2])
    heroes[hero_name] = {"hit_points": hp, "mana_points": mp}

while True:
    command = input()
    if command == "End":
        break
    split_command = command.split(" - ")
    action = split_command[0]

    if action == "CastSpell":
        hero_name = split_command[1]
        mp_needed = int(split_command[2])
        spell_name = split_command[3]

        if mp_needed > heroes[hero_name]["mana_points"]:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes[hero_name]["mana_points"] -= mp_needed
            left = heroes[hero_name]["mana_points"]
            print(f"{hero_name} has successfully cast {spell_name} and now has {left} MP!")

    elif action == "TakeDamage":
        hero_name = split_command[1]
        damage = int(split_command[2])
        attacker = split_command[3]

        if damage >= heroes[hero_name]["hit_points"]:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]

        else:
            heroes[hero_name]["hit_points"] -= damage
            left = heroes[hero_name]["hit_points"]
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {left} HP left!")

    elif action == "Recharge":
        hero_name = split_command[1]
        amount = int(split_command[2])

        if heroes[hero_name]["mana_points"] + amount > 200:
            charge = 200 - heroes[hero_name]["mana_points"]
            heroes[hero_name]["mana_points"] = 200

            print(f"{hero_name} recharged for {charge} MP!")
        else:
            heroes[hero_name]["mana_points"] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif action == "Heal":
        hero_name = split_command[1]
        amount = int(split_command[2])

        if heroes[hero_name]["hit_points"] + amount > 100:
            heal = 100 - heroes[hero_name]["hit_points"]
            heroes[hero_name]["hit_points"] = 100

            print(f"{hero_name} healed for {heal} HP!")
        else:
            heroes[hero_name]["hit_points"] += amount
            print(f"{hero_name} healed for {amount} HP!")

for key, values in heroes.items():
    print(f"{key}")
    print(f"  HP: {values['hit_points']}")
    print(f"  MP: {values['mana_points']}")
