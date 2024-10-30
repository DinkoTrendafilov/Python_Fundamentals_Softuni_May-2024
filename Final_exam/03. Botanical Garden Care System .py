plants_information = {}

while True:
    command = input()
    if command == "EndDay":
        break
    split_command = command.split(": ")
    action = split_command[0]
    plants_info = split_command[1]
    split_plants_info = plants_info.split("-")

    if action == "Plant":
        plant_name = split_plants_info[0]
        water_needed = int(split_plants_info[1])
        section = split_plants_info[2]

        if plant_name not in plants_information:
            plants_information[plant_name] = {"water_needed": water_needed, "section": section}
        else:
            plants_information[plant_name]["water_needed"] += water_needed

    elif action == "Water":
        plant_name = split_plants_info[0]
        water_amount = int(split_plants_info[1])

        if plant_name in plants_information:
            plants_information[plant_name]["water_needed"] -= water_amount
            if plants_information[plant_name]["water_needed"] <= 0:
                print(f"{plant_name} has been sufficiently watered.")
                plants_information.pop(plant_name)

print("Plants needing water:")
for plant_name, info in plants_information.items():
    print(f" {plant_name} -> {info['water_needed']}ml left")

sections_with_thirsty_plants = {}
for info in plants_information.values():
    section = info["section"]
    if section not in sections_with_thirsty_plants:
        sections_with_thirsty_plants[section] = 1
    else:
        sections_with_thirsty_plants[section] += 1

print("Sections with thirsty plants:")
for section, count in sections_with_thirsty_plants.items():
    print(f" {section}: {count}")
