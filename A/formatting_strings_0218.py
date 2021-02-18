name = "Paul York"
phone = "555-1212"

print(name)
print(name.ljust(40))

print(name, phone)
print(name.ljust(40), phone.ljust(40))
print(name[:7].ljust(7), phone[:7].ljust(7))
print(name[:20].ljust(20), phone[:20].ljust(20))

print(name.rjust(30), phone)
print("John Lenon".rjust(30), "555-1313")

print()
print()

print("HEADER TEXT".center(40))
print("-" * 40)
print(name.rjust(30), phone.rjust(10))
print("John Lenon".rjust(30), "555-1313".rjust(10))

print()
print()

print("HEADER TEXT".center(40))
print("-" * 40)
print(name.rjust(30) + phone.rjust(10))
print("John Lenon".rjust(30), end='')
print("555-1313".rjust(10))


print()
print()

print("Hello {}, my name is {}".format("there", "Paul"))
print("I am {} years old and weigh {:.2f} pounds".format(29, 165.20714))

greet = "there"
name = "Paul"
age = 29
weight = 165.20714

print(f"Hello {greet}, my name is {name}")
print(f"I am {age} years old and weigh {weight:.2f} pounds")

title = "CONTACTS"

print()
print()

# FORMAT STRING
#  value : alignment size precision datatype
#     alignment:  <    left
#                 >    right
#                 ^    center
#          e.g.:  <30   left align in 30 spaces
#                 ^60   center in 60 spaces
#     datatype:   f     float
#     precision:  .something   how many decimals to round to

print(f"{title:^80}")
print("=" * 80)
print(f"{name:40}{age:>20}{weight:>20.2f}")
print(f"{name:40}{age:>20.2f}{weight:>20.2f}")

price = 12.7

print(f"$ {price:.2f}")

price_str = f"$ {price:.2f}"
print(f"{price_str:>20}")
