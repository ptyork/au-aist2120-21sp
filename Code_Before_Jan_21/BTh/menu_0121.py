while True:
    print("MENU")
    print("====")
    print('1) Print "HI"')
    print("2) Print \"HELLO\"")
    print("A) Count to 10")
    print("B) Summation of N from 1 to N")
    print("X) Exit")

    choice = input("ENTER CHOICE: ")

    # if choice == "X" or choice == "x":

    choice = choice.upper()
    if choice == "X":
        # exit()
        break
    elif choice == "1":
        print("HI")
    elif choice == "2":
        print("HELLO")
    elif choice == "A":
        for cnt in range(1,11):
            print("I KANZ KOUNT " + str(cnt))
    elif choice == "B":
        total = 0
        N = int(input("ENTER N: "))
        for val in range(1,(N+1)):
            print(total, "+", val, "=", end="")
            total = total + val
            print(total)
        print("this summation of N from 1 to", N, "is", total)
    


print("BYEEEEEE")
