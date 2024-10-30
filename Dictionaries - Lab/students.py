students_info = {}
while True:
    command = input()
    if ":" not in command:
        break

    split_command = command.split(":")
    name = split_command[0]
    name_id = split_command[1]
    course = split_command[2]

    if course not in students_info:
        students_info[course] = {}
    students_info[course][name_id] = name

course = " ".join(command.split("_"))

for key, value in students_info.items():
    if key == course:
        for name_id, name in value.items():
            print(f"{name} - {name_id}")
