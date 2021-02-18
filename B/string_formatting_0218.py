name = "Paul York"
age = 29
weight = 165.718282828459045  # 2.718282828459045

print(name, age)
print(name + "\t" + str(age))

name = "Paul York"
age = 29
print(name.ljust(40) + str(age))
name = "Zaphod Beeblebrox"
age = 53
print(name.ljust(40) + str(age))


name = "Paul York"
age = 29
print(name.ljust(10) + str(age))
name = "Zaphod Beeblebrox"
age = 53
print(name.ljust(10) + str(age))



name = "Paul York"
age = 29
print(name[:10].ljust(10) + str(age))
name = "Zaphod Beeblebrox"
age = 53
print(name[:10].ljust(10) + str(age))


print("CONTACTS".center(60))
print("=" * 60)
print("Name".ljust(40), end='')
print("Age".rjust(20))
print('-' * 60)

name = "Paul York"
age = 29
print(name.ljust(40) + str(age).rjust(20))
name = "Zaphod Beeblebrox"
age = 53
print(name.ljust(40) + str(age).rjust(20))


name = "Paul York"
age = 29
weight = 165.718282828459045  # 2.718282828459045
print("Name: {}  Age: {}  Weight: {}".format(name, age, weight))
name = "Zaphod Beeblebrox"
age = 53
weight = 222.14159265358979
print("Name: {}  Age: {}  Weight: {}".format(name, age, weight))

name = "Paul York"
age = 29
weight = 165.718281828459045  # 2.718282828459045
print("Name: {}  Age: {}  Weight: {:.2f}".format(name, age, weight))
name = "Zaphod Beeblebrox"
age = 53
weight = 222.14159265358979
print("Name: {}  Age: {}  Weight: {:.2f}".format(name, age, weight))
print(weight)



name = "Paul York"
age = 29
weight = 165.718281828459045  # 2.718282828459045
print("{:<40}{:>10}{:>10.2f}".format(name, age, weight))
name = "Zaphod Beeblebrox"
age = 53
weight = 222.14159265358979
print("{:<40}{:>10}{:>10.2f}".format(name, age, weight))


name = "Paul York"
age = 29
weight = 165.718281828459045  # 2.718282828459045
print(f"{name:<40}{age:>10}{weight:>10.2f}")
name = "Zaphod Beeblebrox"
age = 53
weight = 222.14159265358979
print(f"{name:<40}{age:>10}{weight:>10.2f}")


# format specifier
#   value : alignment size precision datatype
#       alignment:  <   left
#                   >   right
#                   ^   center
#       datatype:   f   float


print()
print()

# print("CONTACTS".center(60))
print(f"{'CONTACTS':^60}")
print("=" * 60)
# print("Name".ljust(40), end='')
# print("Age".rjust(20))
print(f"{'Name':40}{'Age':>10}{'Weight':>10}")
print('-' * 60)

name = "Paul York"
age = 29
weight = 165.718281828459045  # 2.718282828459045
print(f"{name:<40}{age:>10}{weight:>10.2f}")
name = "Zaphod Beeblebrox"
age = 53
weight = 222.14159265358979
print(f"{name:<40}{age:>10}{weight:>10.2f}")

price = 15
print(f"${price:>15.2f}")

price_str = f"$ {price:.2f}"
print(f"{price_str:>15}")
