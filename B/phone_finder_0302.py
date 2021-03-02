

def isPhoneA(val):
    wasFound = False
    print(f'Checking {val}')
    parts = val.split('-')
    if len(parts) == 3:
        ac = parts[0]
        pr = parts[1]
        nu = parts[2]
        if len(ac) == 3 and len(pr) == 3 and len(nu) == 4:
            if ac.isdecimal() == True and pr.isdecimal() == True and nu.isdecimal() == True:
                wasFound = True
    print(wasFound)
    return wasFound

def isPhoneB(val):
    wasFound = False
    print(f'Checking {val}')
    realNum = ''
    for char in val:
        if char.isdecimal() == True:
            realNum += char
    print(realNum)
    wasFound = len(realNum) == 10
    print(wasFound)
    return wasFound

import re

# REGULAR EXPRESSIONS
#    Sequence of Tokens (and other modifiers) that form a pattern to
#    be matched in a string.
#    Tokens:
#       * a value
#       * a character class
#          * CUSTOM: [...]
#            [AEIOU]  Any UPPER CASE vowel
#            [AEIOUuoiea]  ANY vowel
#            [A-Za-z0-9]   ANY alphanumeric character
#            [A-Fa-f0-9]   Hexadecimal character
#          * PRE-DEFINED
#            \w     word char
#            \d     numeric digit
#            \s     whitespace
#            .      any (except newline)
#            \b     word boundary (not word char OR begin or end string)

#    Quantifier:
#       * CUSTOM 
#           T{n} exacly n of T
#           T{n,m} between (INCLUSIVE) n and m
#       * SPECIAL
#           ? 0 or 1   (iow, OPTIONAL)
#           * 0 to many  (e.g. .*)
#           + 1 to many

# EXAMPLES
#    SIMPLE PHONE: \d{3}[\.\- ]\d{3}[\.\- ]\d{4}
#    SLIGHTLY LESS SIMPLE PHONE: \d{3}[\.\- ]?\d{3}[\.\- ]?\d{4}
#    MORE LESS SIMPLE PHONE: \(?\d{3}\)?[\.\- ]?\d{3}[\.\- ]?\d{4}
#    GOOD PHONE: (\(\d{3}\)|\d{3})[\.\- ]?\d{3}[\.\- ]?\d{4}


def isPhone(val):
    wasFound = False
    print(f'Checking {val}')
    ex = re.compile(r'(\(\d{3}\)|\d{3})[\.\- ]?\d{3}[\.\- ]?\d{4}')
    match = ex.match(val)
    # print(match)
    if match != None:
        wasFound = True
    print(wasFound)
    return wasFound




isPhone('706-555-1212')
isPhone('706 555 1212')
isPhone('706.555.1212')
isPhone('706 555-1212')
isPhone('7065551212')
isPhone('(706) 555-1212')
isPhone('(888) 765-4321')

isPhone('706x555x1212')
isPhone('706555121')
isPhone('7')
isPhone('bubbawuzhe')
isPhone('bubbawuzhere')
isPhone('bub-baw-uzhe')
isPhone('bub baw.uzhe')
isPhone('bub.baw.uzhe')
isPhone('800-CONTACTS')
isPhone('255.255.255.0')
isPhone('(7065551212')
isPhone('706)5551212')
