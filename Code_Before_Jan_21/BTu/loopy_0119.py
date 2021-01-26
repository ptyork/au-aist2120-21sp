while True:     # Infinite loop
    break

while False:    # BOGUS LOOP
    print("HELLO")


# while True:
#     print("INFINITE LOOP")


# cnt = 1
# while True:
#     print("INFINITE LOOP " + str(cnt))
#     # cnt = cnt + 1       # cnt++
#     # cnt + 1     BOGUS...Just an expression
#     cnt += 1   # equivalent to cnt = cnt + 1

cnt = 1
while cnt <= 10:
    print("NOT INFINITE LOOP A " + str(cnt))
    # cnt = cnt + 1       # cnt++
    # cnt + 1     BOGUS...Just an expression
    cnt += 1   # equivalent to cnt = cnt + 1

cnt = 1
while True:
    print("NOT INFINITE LOOP B " + str(cnt))
    cnt += 1   # equivalent to cnt = cnt + 1
    if cnt >= 11:
        break

for counter in range(10):    # 10 is the uppoer bound of the sequence NOT INCLUSIVE
    print("NOT INFINITE LOOP C " + str(counter))

for counter in range(10):    # 10 is the uppoer bound of the sequence NOT INCLUSIVE
    print("NOT INFINITE LOOP D " + str(counter + 1))

for counter in range(1,11):    # 1 is the lower bound, 10 is the uppoer bound of the sequence NOT INCLUSIVE
    print("NOT INFINITE LOOP C " + str(counter))


cnt = 2
while True:
    print("ALL EVENS TO 20 A " + str(cnt))
    cnt += 2   # equivalent to cnt = cnt + 2
    if cnt >= 21:
        break

for counter in range(2,21,2): # start, stop, step
    print("EVENS TO 20 B " + str(counter))
