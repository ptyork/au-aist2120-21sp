studs = [
    "Mickey Mouse",
    "Minnie Mouse",
    "Jerry",
    "Algernon"
]

grades = [
    85,
    65,
    100,
    110
]

name = input("Enter name: ")
name = name.strip()
name = name.title()

found = -1
for i in range(len(studs)):
    if studs[i] == name:
        found = i

if found >= 0:
    grade = grades[found]
    print(f"{name} got a {grade}")
else:
    print(f"There ain't no {name}")


if name in studs:
    found = studs.index(name)
    grade = grades[found]
    print(f"{name} got a {grade}")
else:
    print(f"There ain't no {name}")
