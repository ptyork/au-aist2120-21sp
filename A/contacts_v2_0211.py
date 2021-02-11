# import pprint
# from pprint import pprint   # import one function from the pprint lib
from pprint import pprint as pp  # can also supply an alias

# contacts = []   # I'ma gonna cheat
# contacts = [
#     'Barker,Bob,5551212',
#     'Chaplain,Charlie,5551313'
#     ]

# contacts = {}   # I'ma gonna cheat
contacts = {
    'Barker,Bob': '5551212',
    'Chaplain,Charlie': '5551313'
}


def showcontacts():
    global contacts
    print("MY CONTACTS")
    print("-----------")
    # ITERATE OVER A DICTIONARY TWO WAYS
    # 1) ITERATE OVER THE KEYS COLLECTION
    # for contact in contacts.keys():
    # for name in contacts:         # the default "iterable" is the keys
    #     phone = contacts[name]
    #     print(f"{name} : {phone}")
    # 2) ITERATE OVER THE ITEMS COLLECTION
    for contact in contacts.items():
        # print(contact)
        # name = contact[0]
        # phone = contact[1]
        name, phone = contact
        print(f"{name} : {phone}")

    for name, phone in contacts.items():
        print(f"{name} : {phone}")

def addcontact():
    global contacts
    print("NEW CONTACT")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    
    fullname = f"{lname.strip().title()},{fname.strip().title()}"

    if fullname in contacts:
        print("ALREADY EXISTS!!!")
        return
    
    phone = input("Phone Number: ").strip()

    # ADD (CREATE) TO THE DICTIONARY
    contacts[fullname] = phone

    print(f"Added {fullname}")
    # pprint.pprint(contacts)
    # pprint(contacts)
    pp(contacts)

def updatecontact():
    global contacts

    if len(contacts) == 0:
        print("NO CONTACTS TO EDIT")
        return   # EXIT EARLY

    print("WHICH CONTACT")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    
    fullname = f"{lname.strip().title()},{fname.strip().title()}"

    if fullname not in contacts:
        print("NOBODY HOME!!!")
        return
    
    phone = input("Phone Number: ").strip()

    # UPDATE THE DICTIONARY
    contacts[fullname] = phone

    print(f"Updated {fullname}")
    pp(contacts)


def deletecontact():
    global contacts

    if len(contacts) == 0:
        print("NO CONTACTS TO EDIT")
        return   # EXIT EARLY

    print("WHICH CONTACT")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    
    fullname = f"{lname.strip().title()},{fname.strip().title()}"

    if fullname not in contacts:
        print("NOBODY HOME!!!")
        return
    
    del contacts[fullname]
    pp(contacts)

    print(f"{fullname} has been deleted. Good riddance!")

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
