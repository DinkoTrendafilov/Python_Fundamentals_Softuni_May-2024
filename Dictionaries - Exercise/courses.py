courses = {}

while True:
    command = input()

    if command == "end":
        break

    split_command = command.split(" : ")

    course_name = split_command[0]
    student_name = split_command[1]

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)


for course_name, students_name in courses.items():
    print(f"{course_name}: {len(students_name)}")

    for student_name in students_name:
        print(f"-- {student_name}")



