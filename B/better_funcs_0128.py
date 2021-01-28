# IMPORTS
import random

# GLOBAL VARIABLES
counter = 0

# FUNCTIONS
def recursiveHello():
    global counter
    print("Hello", counter)
    counter += 1
    if counter < 10:
        recursiveHello()
    print("Exit recursiveHello", counter)

def getString(minlen,maxlen):
    while True:
        val = input("Enter a string: ")
        val = val.strip()
        if len(val) < minlen:
            print("Too short. Try again.")
            continue
        if len(val) > maxlen:
            print("Too long. Try again.")
            continue
        return val

def getInt():
    while True:
        val = input("Enter an integer: ")
        try:
            intval = int(val)
        except:
            print("I said an integer you moron! Try again")
            continue
        return intval

def getCard():
    suitVal = random.randint(1,4)
    faceVal = random.randint(1,13)

    suit = "Hearts"
    if suitVal == 1:
        suit = "Clubs"
    elif suitVal == 2:
        suit = "Spades"
    elif suitVal == 3:
        suit = "Diamonds"
    # elif suitVal == 4:
    #     suit = "Hearts"
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
    # REAL CODE GOES HERE (Entrypoint)
    # recursiveHello()       # Uncomment if you wanna play with recursion
    print("What is your name? ")
    name = getString(2,30)
    print(f"Oh, hi there {name}!!")

    print("What is your age?")
    age = getInt()
    print(f"Oh, you're only {age}, I'm {age + 2}!!")

    mycard = getCard()
    print(f"COOL. You drew a {mycard}!!!!")
    mycard = getCard()
    print(f"COOL. You drew a {mycard}!!!!")
    mycard = getCard()
    print(f"COOL. You drew a {mycard}!!!!")
    mycard = getCard()
    print(f"COOL. You drew a {mycard}!!!!")
    mycard = getCard()
    print(f"COOL. You drew a {mycard}!!!!")


main()
