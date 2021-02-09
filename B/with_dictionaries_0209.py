# 1 Dictionary instad of  2 lists
stud_grade = {
    "Mickey Mouse": 85,
    "Minnie Mouse": 65,
    "Jerry": 100,
    "Algernon": 110
}

name = input("Enter name: ")
name = name.strip()
name = name.title()

# if name in stud_grade.keys():     #search the keys
# if name in stud_grade.values():   #search the values
if name in stud_grade:              #search the keys
    grade = stud_grade[name]
    print(f"{name} got a {grade}")
else:
    print(f"There ain't no {name}")


# grade = stud_grade[name]
# print(f"{name} got a {grade}")



studs_with_grade = {
    110: ["Algernon"],
    100: ["Jerry"],
    85: ["Mickey Mouse"],
    65: ["Minnie Mouse","Bob"],
    0: []
}


grade = 110

matches = studs_with_grade[grade]
for stud in matches:
    print(stud + " got a 110")

grade = 65

matches = studs_with_grade[grade]
for stud in matches:
    print(stud + " got a 65")


for grade in studs_with_grade:      # iterate over all of the keys
    matches = studs_with_grade[grade]
    for stud in matches:
        print(f"{stud} got a {grade}")
