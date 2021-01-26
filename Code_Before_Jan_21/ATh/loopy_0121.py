while True:    # infinite loop
    print("HI")
    break

while False:    # BOGUS/DUMB/NO/BAD
    print("HO")

# counter = 1
# while True:
#     print("INFINITE LOOP " + str(counter))
#     # counter = counter + 1   # counter++
#     counter += 1    # SAME AS counter = counter + 1
#     # counter + 1    NO...JUST AN EXPRESSION

counter = 1
while True:
    print("NOT INFINITE LOOP A " + str(counter))
    counter += 1    # SAME AS counter = counter + 1
    if counter > 10:
        break

counter = 1
while counter < 11:
    print("NOT INFINITE LOOP B " + str(counter))
    counter += 1    # SAME AS counter = counter + 1


# nums = int[..]
# foreach (int num in nums)

for cnt in range(10):
    print("NOT INFINITE LOOP C " + str(cnt))

for cnt in range(10):
    print("NOT INFINITE LOOP D " + str(cnt+1))

for cnt in range(1,11):
    print("NOT INFINITE LOOP E " + str(cnt))

for cnt in range(1,11):
    print("EVENS A " + str(cnt*2))

for cnt in range(2,21,2):
    print("EVENS B " + str(cnt))

counter = 2
while counter < 21:
    print("EVENS C " + str(counter))
    counter += 2    # SAME AS counter = counter + 2

