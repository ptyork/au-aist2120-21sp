import time

epoch = time.time()

print(epoch)

for i in range(25):
    print(i, time.time_ns())


# ELAPSED TIME

curr = time.time()

j = 0
for i in range(1000000):
    if i % 2 == 0:
        j = j + i
    else:
        j = j - i
print(j)

elapsed = time.time() - curr
print(f"ELAPSED: {elapsed}s")


def pauseOne():
    curr = time.time()
    while True:
        elapsed = time.time() - curr
        if elapsed >= 1:
            break
    return

for i in range(5,0,-1):
    print(i)
    # pauseOne()
    # time.sleep(1)
print("BLASTOFF!!!")

# WRAPPER AROUND TIME FOR FANCY STUFF

from datetime import datetime

now = datetime.now()
print(now)
print(type(now))

bday = datetime(1972,4,20,20,35)
print(bday)

print(bday.weekday())

friendly = bday.strftime('%A, %B %d, %Y')

print(friendly)

age = now - bday

print(age)
print(type(age))

ageyears = age.days / 365.25
print(ageyears)

import math
ageyears = math.floor(ageyears)

print(ageyears)

print(int(44.6))

