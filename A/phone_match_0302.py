import re

p1 = "706-555-1212"
p2 = "706 555 1212"
p3 = "(706) 555-1212"
np1 = "bob-isn-opho"

def isPhoneOld(val):
    print(f'Testing {val}')
    # parts = val.split('-')
    # if len(parts) != 3:
    #     return False
    v = val.replace('-', '')
    v = v.replace(' ', '')
    v = v.replace('(', '')
    v = v.replace(')', '')
    # print(v)
    # print(v.isdecimal())
    match = v.isdecimal() == True and len(v) == 10
    return match

def isPhone(val):
    print(f'Testing {val}')
    ex = re.compile(r'(\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}')
    # print(ex.match(val))
    match = ex.match(val)
    found = match != None
    return found

print(isPhone(p1))
print(isPhone(p2))
print(isPhone(p3))
print(isPhone(np1))
print(isPhone('555-1212'))
print(isPhone('12'))
print(isPhone('1-800-Contacts'))


# Regular Expressions
#   a "string" pattern to be matched
#    * characters can be exact match OR a character class
#      pre-defined char class (e.g., \d or \w)
#      custom char class (e.g.
#         [aeiou]   class = LOWER CASE vowels
#         [AEIOUaeiou]   class = ALL vowels
#         [A-Fa-f]   character ranges
#         [A-Fa-f0-9]   HEXADECIMAL digit
#      quantifiers
#         custom  {3} exactly 3 or {3,5} between 3 and 5
#         ?   matches MAYBE one (0,1})
#         +   one or more of the preceeding token
#         *   match as many or none as you find


# EXAMPLE
#  HEX COLOR: #?[A-Fa-f0-9]{3,6}
#  SIMPLE PHONE:  \(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}
#  HARDER PHONE:  (\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}
