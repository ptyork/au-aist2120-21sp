while True:
    print("MENU")
    print("1) SAY HI")
    print("2) SAY LOW")
    print("A) COUNT TO 10")
    print("B) CALCULATE SUMMATION OF N")
    print("X) Exit")

    choice = input("CHOOSE: ")

    # if choice == "X":
    # if choice == "X" or choice == "x":
    choice = choice.upper()
    choice = choice.strip()

    if choice == "X":
        break
        # exit()
    elif choice == "1":
        print("HI")
    elif choice == "2":
        print("LOW")
    elif choice == "A":
        for counter in range(1,11):
            print("yo " + str(counter))
    elif choice == "B":
        n = int(input("Enter N: "))
        total = 0   # running subtotal (accumulator)
        for num in range(1,n+1):   # Count from 1 to 5
            print(str(total) + " + " + str(num) + " = ", end='')
            total = total + num
            print(total)

        print("Summation of " + str(n) + " is " + str(total))
