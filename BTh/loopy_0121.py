while True:    # infinite
    print("HI")
    break

while False:    # BOGUS Loop
    print("HO")


# counter = 1
# while True:
#     print("INFINTE LOOP " + str(counter))
#     # counter = counter + 1 # counter++
#     counter += 1
#     # counter + 1   NOPE JUST AN EXPRESSION

counter = 1
while counter < 11:
    print("NOT INFINTE LOOP A " + str(counter))
    counter += 1

counter = 1
while True:
    print("NOT INFINTE LOOP B " + str(counter))
    counter += 1
    if counter >= 11:
        break

# C#
# nums = [1,2,3,4,5];
# foreach (int num in nums) {
#     Console.Writeline(num);
# }

for cnt in range(10):
    print("NOT INFINITE LOOP C " + str(cnt))

for cnt in range(10):
    print("NOT INFINITE LOOP D " + str(cnt+1))

for cnt in range(1,11):
    print("NOT INFINITE LOOP E " + str(cnt))

for cnt in range(1,11):
    print("EVENS FROM 2 TO 20 A: " + str(cnt*2))

counter = 2
while True:
    print("EVENS FROM 2 TO 20 B: " + str(counter))
    counter += 2
    if counter >= 21:
        break

for cnt in range(2,21,2):
    print("EVENS FROM 2 TO 20 C: " + str(cnt))

print(cnt, "IS STILL HERE")   # YUCK SCOPE

