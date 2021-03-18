import sys

# print(sys.argv) 

# NOTE: argv[0] is always the name of the script file
# argv[1+] are arguments to your script

fn = sys.argv[2]
tofind = sys.argv[1]
tofind = tofind.lower()

with open(fn) as fi:
    linenum = 0
    for line in fi:
        linenum += 1
        line = line.rstrip()
        tmpline = line.lower()
        if tofind in tmpline:
            print(f"{linenum}: {line}")
