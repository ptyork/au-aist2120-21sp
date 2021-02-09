students = [
    'Alice',
    'Bob',
    'Chuck',
    'Dr. Dre'
]

grades = [
    85,
    70,
    60,
    100    
]

name = input("Enter name: ")
name = name.strip()
name = name.title()   # auto capitalize each word

if name in students:
    idx = students.index(name)    # find name

    grade = grades[idx]

    print(f"{name} has a {grade}")
else:
    print(f"{name} ain't here")


# CHALLENGE (CASE INSENSITIVE SEARCH)

students = [
    'AlIcE',
    'BOB',
    'chuck',
    'DR. DRE'
]

# for x in range....:
#   name is students[x]
#   if name (case insensitive) matches
#     break

# Do the above to replicate our solution


