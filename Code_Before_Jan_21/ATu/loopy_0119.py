while True:   # Infinite / non-terminating loop construct
    break     # early termination statement

while False:  # BOGUS!!
    print("Hello")

# cnt = 1
# while True:
#     print("INFINITE " + str(cnt))
#     cnt = cnt + 1

cnt = 1
while True:
    print("NOT INFINITE A " + str(cnt))
    cnt = cnt + 1
    if cnt > 10:
        break

cnt = 1
while cnt <= 10:
    print("NOT INFINITE B " + str(cnt))
    # cnt = cnt + 1
    # cnt + 1  NOT ENOUGHT...JUST AN EXPRESSION
    cnt += 1 # IDENTICAL TO cnt = cnt + 1

for counter in range(10):
    print("NOT INFINITE C " + str(counter))

for counter in range(1,11):
    print("NOT INFINITE D " + str(counter))

for counter in range(10):
    print("NOT INFINITE E " + str(counter + 1))


cnt = 2
while True:
    print("EVENS A " + str(cnt))
    cnt = cnt + 2
    if cnt > 20:
        break

for counter in range(2,21,2):
    print("EVENS B " + str(counter))
