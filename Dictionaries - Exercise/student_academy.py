number_of_students = int(input())

students = {}

for _ in range(number_of_students):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

for student, grade in students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade < 4.5:
        continue
    print(f"{student} -> {average_grade:.2f}")

