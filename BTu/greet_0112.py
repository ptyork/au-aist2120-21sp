print("AWESOME GREETER")

# OPTION 1
print("Enter your first name: ")
fname = input()

print("Hello " + fname)

# OPTION 2 (BETTER IMO)
lname = input("Enter your last name: ")

print("Hello " + fname + " " + lname)

age_str = input("Enter your age: ")
age = int(age_str)
real_age = age * 2
print("Yeah right, you're really " + str(real_age))

print('#' * 80)  # string repetition
