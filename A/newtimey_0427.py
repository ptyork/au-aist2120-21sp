# TIME STUFF

import time

now = time.time()

print(f"hi it's {now}")

while True:
    newnow = time.time()
    elapsed = newnow - now
    if elapsed > 1:
        break

print(f"It has ben {elapsed} seconds")


for i in range(25):
    print(i, time.time())

# ABOVE IS CPU INTENSIVE BUT MAY BE NEEDED

# BELOW IS BEST IF YOU'RE TRULY JUST WAITING

now = time.time()
print(f"hi it's {now}")
time.sleep(1)
newnow = time.time()
elapsed = newnow - now
print(f"It has ben {elapsed} seconds")

# "Real" dates and times

from datetime import datetime

print(datetime.now())


now = datetime.now()

past = datetime(1972, 4, 20, 20, 8)

age = now - past
print(type(age))
print(age)

years = age.days / 365.25

print(years)

import math
years = math.floor(years)

print(years)

now = datetime.now()
now_str = now.strftime('%Y-%m-%d')

print(now_str)

now_str = now.strftime('%m-%d-%y')

print(now_str)

