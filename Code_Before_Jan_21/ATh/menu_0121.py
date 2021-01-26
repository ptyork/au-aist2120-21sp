while True:
    print("MENU")
    print('====')
    print('1) SAY "HI"')
    print("2) SAY \"HELLO\"")
    print("A) Count to 10")
    print("B) Summation of n from 1 to n")
    print("X) Exit")

    choice = input("CHOOSE: ")

    # if choice == 'X' or choice == 'x':

    choice = choice.lower()
    choice = choice.strip()   # removes leading and trailing spaces
    if choice == 'x':
        break
        # exit()    EXITS COMPLTELY -- NO BYEEEE
    elif choice == "1":
        print("HI")
    elif choice == "2":
        print("HELLO")
    elif choice == "a":
        for cnt in range(1,11):
            print("COUNT NUMBER " + str(cnt))
    elif choice == "b":
        total = 0
        n = int(input("Enter N: "))
        for num in range(1,(n+1)):
            print(str(total) + " + " + str(num) + " = ", end='')
            total = total + num
            print(total)
        print(total)

print("BYEEEEE")
