def print_backwards(txt):
    rtxt = txt[::-1]
    print(rtxt)


# open('autumn.txt', 'rt')
fn = 'autumn.txt'
fi = open(fn)

# READ IT ALL IN AT ONCE (memory hog)
# content = fi.read()
# print(content)

# READ ONE LINE AT A TIME
# line = fi.readline()
# line = line.rstrip()
# print(line)

# line = fi.readline()
# line = line.rstrip()
# print(line)

# line = fi.readline()
# line = line.rstrip()
# print(line)

# ITERATE OVER THE LINES IN THE FILE

# Filter Example
for line in fi:
    line = line.rstrip()
    if "the" in line:
        print(line)

# Uh oh, the file was already consumed (at end of stream)

fi.close()

fi = open(fn)

# Modify the line Example
for line in fi:
    line = line.rstrip()
    print_backwards(line)

fi.close()
