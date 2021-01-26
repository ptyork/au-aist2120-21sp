while True:
    print("=" * 40)
    print("1) Say Hi")
    print("2) Say Hello")
    print("A) Count to 10")
    print("B) Summation of N")
    print("X) Exit")
    print("-" * 40)
    
    choice = input("ENTER CHOICE: ")
    choice = choice.upper()
    choice = choice.strip()  # removes all leading and trailing spaces

    if choice == "X":
        break
        # exit()
    elif choice == "1":
        print("HI")
    elif choice == "2":
        print("HELLO")
    elif choice == "A":
        for counter in range(1,11):    # 1 is the lower bound, 10 is the uppoer bound of the sequence NOT INCLUSIVE
            print("COUNT SAYS " + str(counter))
    elif choice == "B":
        n = int(input("ENTER N: "))
        total = 0   # Acuumulates the total sum
        for num in range(1,n+1):
            print(total, "+", num, "= ", end='')
            total += num
            print(total)
        print("The summation from 1 to " + str(n) + " of n is", total)

print("SEE YA!!")