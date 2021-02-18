contacts = [
    'Barker,Bob,5551212,88',
    'Chaplain,Charlie,5551313,173',
    'York,Paul,5551414,29'
]

for c in contacts:
    # c is the whole string, e.g. 'Barker,Bob,5551212,88'
    parts = c.split(',') # list of all parts ["Barker","Bob","5551212","88"]
    print(f"{parts[1]} {parts[0]}  {parts[3]}  {parts[2]}")

print()

print("CONTACTS".center(80))
print(f"{'CONTACTS':^80}")
print("=" * 80)
print("Name".center(40) + "Age".center(20) + "Phone".center(20))
print(f"{'Name':^40}{'Age':^20}{'Phone':^20}")
print('-' * 80)
for c in contacts:
    # c is the whole string, e.g. 'Barker,Bob,5551212,88'
    parts = c.split(',') # list of all parts ["Barker","Bob","5551212","88"]
    name = parts[1] + " " + parts[0]
    print(f"{name:40}{parts[3]:>20}{parts[2]:>20}")

print()
print()

print(f"{'CONTACTS':^80}")
print("=" * 80)
print(f"{'Name':<40}{'Age':>20}{'Phone':>20}")
print('-' * 80)
for c in contacts:
    # c is the whole string, e.g. 'Barker,Bob,5551212,88'
    lname, fname, phone, age = c.split(',') # unpack or unwrap the parts
    name = fname + " " + lname
    name = f"{fname} {lname}"
    print(f"{name:40}{age:>20}{phone:>20}")

