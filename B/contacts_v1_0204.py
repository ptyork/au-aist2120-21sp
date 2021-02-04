# contacts = []
contacts = ['alda,alan,5551212', 'barker,bob,5551313']

def addContact():
    global contacts
    print("ADD NEW CONTACT")
    print("---------------")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    phone = input("Phone Number: ")
    contact = f"{lname},{fname},{phone}"
    contacts.append(contact)
    print(f"Added {contact}")
    # print(contacts)     # COMMENTED OUT THIS "DEBUG" PRINT LINE


def displayContacts():
    global contacts
    print("MY CONTACTS")
    print("-----------")
    # 1) Itterate using indexes
    # Possible to alter the value of the elements
    for idx in range(len(contacts)):
        contact = contacts[idx]
        # contacts[idx] = contact + ",test@test.com"
        print(contact)
    # 2) Enumerate the values
    # READ-ONLY
    for contact in contacts:
        # contact = contact + ",test@test.com"
        print(contact)


def updateContact():
    print("Update a Contact")
    print("Choose Contact")
    print("--------------")
    for idx in range(len(contacts)):
        contact = contacts[idx]
        print(f"{idx+1}) {contact}")
    choice = input("Which Contact: ").strip()
    try:
        choicenum = int(choice)
        choicenum -= 1    # convert from human to computerese

        oldContact = contacts[choicenum]
        print(f"Editing {oldContact}...")
        fname = input("Updated First Name: ")
        lname = input("Updated Last Name: ")
        phone = input("Updated Phone Number: ")
        updatedContact = f"{lname},{fname},{phone}"
        
        # Update existing contact
        contacts[choicenum] = updatedContact

        print(f"Updated {oldContact} to {updatedContact}")

    except IndexError:
        print("That number is out of range")
    except ValueError:
        print("I said a number you boob!!")
    except:
        print("Uh oh, something weird happened.")


def deleteContact():
    print("Delete a Contact")
    print("Choose Contact")
    print("--------------")
    for idx in range(len(contacts)):
        contact = contacts[idx]
        print(f"{idx+1}) {contact}")
    choice = input("Which Contact: ").strip()
    try:
        choicenum = int(choice)
        choicenum -= 1    # convert from human to computerese
        # del contacts[choicenum]
        removed = contacts.pop(choicenum)
        print(f"Cool! {removed} has been removed")
    except IndexError:
        print("That number is out of range")
    except ValueError:
        print("I said a number you boob!!")
    except:
        print("Uh oh, something weird happened.")


while True:
    print()
    print("CONTACT MANAGER 2K")
    print("==================")
    print("1) Add a Contact")
    print("2) Display All Contacts")
    print("3) Update a Contact")
    print("4) Delete a Contact")
    print("X) Exit")
    print("-------------------")

    choice = input("Enter Choice: ").strip().upper()

    if choice == "X":
        break
    elif choice == "1":
        addContact()
    elif choice == "2":
        displayContacts()
    elif choice == "3":
        updateContact()
    elif choice == "4":
        deleteContact()
    else:
        print("INVALID CHOICE")
        