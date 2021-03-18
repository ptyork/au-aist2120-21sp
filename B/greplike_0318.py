import sys

# sys.stdout.write("What is your name: ")
# sys.stdout.flush()
# name = sys.stdin.readline().strip()
# sys.stdout.write(f"Hi {name}")
# sys.stdout.flush()

# sys.exit()

if len(sys.argv) != 2:
    print("You are stoooopid")
    sys.exit()

tofind = sys.argv[1]
tofind = tofind.lower()



linenum = 0
for line in sys.stdin:
    linenum += 1
    line = line.rstrip()
    tmpline = line.lower()
    if tofind in tmpline:
        print(f"{linenum}: {line}")
