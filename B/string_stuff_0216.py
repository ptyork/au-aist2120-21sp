"Single Line"
'Single Line'
'''
Multi-Line
'''
a = "apple"
f"I like {a} pie (FORMATTED STRING)"
r"RAW STRING"

print("new\nline")
print("1\t2\t3\t4")
print("It is a \"HOT\" day")
print('It\'s a "HOT" day')
print('We meet Tue\Thu')
print('We are old\new')
print('We are old\\new')

print(r"new\nline")
print(r"1\t2\t3\t4")
print(r"It is a \"HOT\" day")
print(r'It\'s a "HOT" day')
print(r'We meet Tue\Thu')
print(r'We are old\new')
print(r'We are old\\new')


# Strings a a squence of numbers

let = "a"
num = ord(let)
print(num)
print(chr(num))
let = "A"
num = ord(let)
print(num)
print(chr(num))
let = "5"
num = ord(let)
print(num)
print(chr(num))

text = "hello there 019az"

enc_text = ""

for let in text:
    let_val = ord(let)
    enc_val = let_val - 1
    enc_char = chr(enc_val)
    enc_text = enc_text + enc_char

print(enc_text)

dec_text = ""

for let in enc_text:
    let_val = ord(let)
    dec_val = let_val + 1
    dec_char = chr(dec_val)
    dec_text = dec_text + dec_char

print(dec_text)

# Changing a string (NO get a COPY and change that)

t = "Hello worlD"
print(t.upper())
print(t.lower())
print(t.capitalize())
print(t.title())


# Query a string
print('12'.isdigit())
print('12'.isnumeric())
print('12'.isdecimal())

print('1.2'.isdigit())
print('1.2'.isnumeric())
print('1.2'.isdecimal())

print('12½'.isdigit())
print('12½'.isnumeric())
print('12½'.isdecimal())

print('12½'.isascii())
print('12'.isascii())

# FINDING / SEARCHING "SUBSTRINGS"

s = "the rain in spain falls mainly on the plain"

print("the" in s)
print("the" not in s)
print(not "the" in s)

print(s.startswith("the"))      # True
print(s.endswith("the"))        # False
print(s.startswith("ain"))      # False
print(s.endswith("ain"))        # True
print(s.endswith("e plain"))    # True

# HOW MANY

print(s.count("a"))
print(s.count("the"))
print(s.count("ain"))

# FIND THE FIRST LOCATION OF "ain"

for i in range(len(s)):
    # let = s[i]
    # print(let)
    if s[i] == 'a':
        if s[i+1] == 'i':
            if s[i+2] == 'n':
                print(i)
                break

loc = s.index('ain')
print(loc)
# loc = s.index('butt')    # blowups happen
# print(loc)

loc = s.find('ain')
print(loc)
sub = s[loc:]
print(sub)
loc = s.find('butt')
print(loc)
sub = s[loc:]
print(sub)



tofind = 'ain'
loc = s.find(tofind)
before = s[:loc]
word = s[loc:loc+len(tofind)]
after = s[loc+len(tofind):]
print(before)
print(word)
print(after)


tofind = 's'
loc = s.find(tofind)
before = s[:loc]
word = s[loc:loc+len(tofind)]
after = s[loc+len(tofind):]
print(before)
print(word)
print(after)


print(s.partition("ain"))
# parts = s.partition("ain")
before, word, after = s.partition("ain")   # unpack / unwrap
print(before)
print(word)
print(after)


words = s.split(" ")
print(words)

s = '''
the rain in spain falls
mainly on the plain
'''

words = s.split(" ")
print(words)

words = s.split()
print(words)


data = "80,90,100,75"

total = 0
vals = data.split(',')
print(vals)

for val_str in vals:
    val = int(val_str)
    total += val

print(total)
average = total / len(vals)
print(average)


int_vals = [int(v) for v in vals]
print(int_vals)

int_vals = [int(v) for v in vals if int(v) < 100]
print(int_vals)

int_vals = [100 for v in vals]
print(int_vals)

vals = ["100" for v in vals]
print(vals)
