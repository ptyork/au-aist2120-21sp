student_grade = {
    "Alice": 85,
    "Bob": 70,
    "Chuck": 60,
    "Dr. Dre": 100
}

name = input("Enter name: ")
name = name.strip()
name = name.title()   # auto capitalize each word

# grade = student_grade[name]

# if name in student_grade.values():  # search values
# if name in student_grade.keys():  # search keys
if name in student_grade:  # search keys
    grade = student_grade[name]
    print(f"{name} has a {grade}")
else:
    print(f"{name} ain't here")


students_with_grade = {
    100: ['Dr. Dre', 'Jiggy', 'Mary Poppins'],
    85: ['Alice'],
    70: ['Bob'],
    60: ['Chuck'],
    50: []
}


grade_str = input("Enter grade: ").strip()

grade = int(grade_str)

if grade in students_with_grade:
    students = students_with_grade[grade]
    for stu in students:
        print(stu)
else:
    print(f"no students with {grade}")