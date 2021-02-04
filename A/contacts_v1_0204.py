# contacts = []   # I'ma gonna cheat
contacts = ['Barker,Bob,5551212', 'Chaplain,Charlie,5551313']

def showcontacts():
    global contacts
    print("MY CONTACTS")
    print("-----------")
    # ITTERATE OVER THE SEQUENCE (LIST)
    # AKA ENUMERATE THE LIST
    for x in range(len(contacts)):
        # using the numbered index is useful IF you want
        # to change any of the values
        contact = contacts[x]
        # contacts[x] = "bubba"   HOW TO ALTER THE VALUE OF THE ELEMENTS OF A LIST
        print(contact)
    for contact in contacts:
        # without the index is a bit clear but read-only
        # contact = "bubba" doesn't work
        print(contact)

def addcontact():
    global contacts
    print("NEW CONTACT")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    phone = input("Phone Number: ")
    contact = f"{lname},{fname},{phone}"
    contacts.append(contact)
    print(f"Added {contact}")
    print(contacts)

def updatecontact():
    global contacts

    if len(contacts) == 0:
        print("NO CONTACTS TO EDIT")
        return   # EXIT EARLY

    print("SELECT CONTACT")
    print("--------------")
    for idx in range(len(contacts)):
        contact = contacts[idx]
        print(f"{idx+1}) {contact}")
    choicestr = input("SELECTION: ")
    try:
        choice = int(choicestr)
        choice -= 1    # convert from human back to computerese

        oldcontact = contacts[choice]
        print(f"Editing {oldcontact}")

        fname = input("Updated First Name: ")
        lname = input("Updated Last Name: ")
        phone = input("Updated Phone Number: ")
        updatedcontact = f"{lname},{fname},{phone}"
        # OVERWRITE the old value with the new value
        contacts[choice] = updatedcontact
        print(f"Changed {oldcontact} to {updatedcontact}")
    except ValueError:
        print("That ain't no number")
    except IndexError:
        print("That's not a valid value")

def deletecontact():
    global contacts

    if len(contacts) == 0:
        print("NO CONTACTS TO DELETE")
        return   # EXIT EARLY

    print("SELECT CONTACT")
    print("--------------")
    for idx in range(len(contacts)):
        contact = contacts[idx]
        print(f"{idx+1}) {contact}")
    choicestr = input("SELECTION: ")
    try:
        choice = int(choicestr)
        choice -= 1    # convert from human back to computerese
        # del contacts[choice]
        deleted = contacts.pop(choice)
        print(f"{deleted} was deleted")
    except ValueError:
        print("That ain't no number")
    except IndexError:
        print("That's not a valid value")

# MENU
while True:
    print()
    print("CONTACT MANAGER 2000")
    print("====================")
    print("1) Show Contacts")
    print("2) Add Contact")
    print("3) Update Contact")
    print("4) Delte Contact")
    print("X) Exit")
    print("--------------------")
    choice = input("Enter your choice: ").upper()
    
    if choice == "X":
        break
    elif choice == "1":
        showcontacts()
    elif choice == "2":
        addcontact()
    elif choice == "3":
        updatecontact()
    elif choice == "4":
        deletecontact()
    else:
        print("INVALID SELECTION")
