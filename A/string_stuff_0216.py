"one line"
'one line'
'''
multi line
'''
a = "apple"
f"{a}"
r"RAW UNESCAPED STRING"

"new \n line"
"\" HELLO \""
'IT\'S A VERY HOT SPOT'
'name\taddress'
print('1\t2\t3\t4')
print('Male\\Female\\Other')
print(r'Male\\Female\\Other')
print(r'Male\Female\Other')


# CONVERSION TO NUMS

print("A")
print(ord("A"))
print(ord("a"))
print(chr(65))

h = "hello"

# encrypt

h1 = ""
for let in h:
    enc = ord(let) - 1
    h1 += chr(enc)
print(h1)

# decrypt

h2 = ""
for let in h1:
    dec = ord(let) + 1
    h2 += chr(dec)
print(h2)

# QUERY

s = "the rain in spain falls mainly on the plain"

print("the" in s)
print("The" in s)

cnt = 0

for i in range(len(s)):
    # print(s[i])
    if s[i] == "t":
        if s[i+1] == "h":
            if s[i+2] == "e":
                cnt += 1

print(cnt)

# or the easy way
print(s.count("the"))
print(s.count("ain"))

print(s.startswith("the"))
print(s.startswith("plain"))
print(s.endswith("the"))
print(s.endswith("plain"))


# [].index()
print(s.index('ain'))
print(s.index('pain'))
# print(s.index('splain'))

print(s.find('ain'))
print(s.find('pain'))
print(s.find('splain'))

loc = s.find("ain")
print(s[loc])
loc = s.find("pain")
print(s[loc])
loc = s.find("splain")
print(s[loc])

# SUBSTRING

loc = s.find(" in ")  # find only the whole word...returns loc of space
before = s[0:loc]
after = s[loc:].lstrip()
print(before)
print(after)

print(s.partition(" in "))

before, middle, after = s.partition(" in ")  # unpack/unwrap
print(before + middle + after)

print(s.split(" "))
print(s.split("ain"))
print(s.split("the"))

data = "70,80,100,80"

total = 0
cnt = 0
for val_str in data.split(","):
    total += int(val_str)
    cnt += 1
average = total / cnt
print(average)


