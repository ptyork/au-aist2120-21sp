contacts = [
    'alda,alan,5551212,72',
    'barker,bob,5551313,99',
    'york,paul,5551414,29'
]


print(f"{'CONTACTS':^80}")
print('=' * 80)
print(f"{'Name':<50}{'Age':>15}{'Phone Number':>15}")
print('-' * 80)
for c in contacts:
    # print(c)
    parts = c.split(',')
    # print(parts)

    # joined = '\t\t'.join(parts)
    # print(joined)
    # joined = ''.join(parts)
    # print(joined)

    fullname = parts[1] + ' ' + parts[0]
    age = parts[3]
    phone = parts[2]
    phone = phone[:3] + '-' + phone[3:]

    print(f"{fullname.title():<50}{age:>15}{phone:>15}")

print('=' * 80)


print()
print()

print(f"{'CONTACTS':^80}")
print('=' * 80)
print(f"{'Name':<50}{'Age':>15}{'Phone Number':>15}")
print('-' * 80)
for c in contacts:
    lname, fname, phone, age = c.split(',')

    fullname = fname + ' ' + lname
    phone = phone[:3] + '-' + phone[3:]

    print(f"{fullname.title():<50}{age:>15}{phone:>15}")

print('=' * 80)
