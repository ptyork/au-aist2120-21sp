import random

rcounter = 0

def recursiveHello():
    global rcounter
    print("Enter rH", rcounter)
    rcounter += 1
    if rcounter < 10:
        recursiveHello()
    print("Exit rH", rcounter)


def getString(minSize, maxSize):
    while True:    # exit manually if and only if there is a valid string input
        val = input("Enter string: ")
        val = val.strip()
        if len(val) < minSize:
            print("Too short, try again")
            continue
        if len(val) > maxSize:
            print("Too long, try again")
            continue
        return val


def getInt():
    while True:
        val = input("Enter integer: ")
        val = val.strip()  # doh, turns out this isn't really needed
        try:
            intVal = int(val)
        except:
            print("That ain't no int. Try again.")
            continue
        return intVal


def getCard():
    suitVal = random.randint(1,4)
    faceVal = random.randint(1,13)
    
    suit = "Hearts"
    if suitVal == 1:
        suit = "Spades"
    elif suitVal == 2:
        suit = "Clubs"
    elif suitVal == 3:
        suit = "Diamonds"
    # else:
    #     suit = "Hearts"
    
    face = "Ace"
    if faceVal >= 2 and faceVal <= 10:
        face = str(faceVal)
    elif faceVal == 11:
        face = "Jack"
    elif faceVal == 12:
        face = "Queen"
    elif faceVal == 13:
        face = "King"
    
    card = f"{face} of {suit}"
    return card


def main():
    # main execution function
    # recursiveHello()   # Uncomment this for FUNNNNN
    print("What is your name?")
    name = getString(2,30)
    print(f"Oh, hi there {name}")

    print("How old are you?")
    age = getInt()
    print(f"Dang! You're only {age}. I'm {age + 5}.")

    card = getCard()
    print(f"Congratulations, you drew a {card}")
    card = getCard()
    print(f"Congratulations, you drew a {card}")
    card = getCard()
    print(f"Congratulations, you drew a {card}")
    card = getCard()
    print(f"Congratulations, you drew a {card}")
    card = getCard()
    print(f"Congratulations, you drew a {card}")


main()  # kick off the program