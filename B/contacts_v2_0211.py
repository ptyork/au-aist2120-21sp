# import pprint                   # import a module
# from pprint import pprint       # import a function from a module
from pprint import pprint as pp   # optionally give the function an alias

# contacts = []
# contacts = ['alda,alan,5551212', 'barker,bob,5551313']

contacts = {
    'alda,alan': '5551212', 
    'barker,bob': '5551313'
}


def displayContacts():
    global contacts
    print("MY CONTACTS")
    print("-----------")
    # 1) Itterate explicitly over the keys
    # for name in contacts.keys():
    for name in contacts:
        phone = contacts[name]
        print(f"{name} : {phone}")
    for ctct in contacts.items():
        # print(ctct)
        # unpacking the tuple into variables
        name = ctct[0]
        phone = ctct[1]
        print(f"{name} : {phone}")
    for ctct in contacts.items():
        # unpacking the tuple into variables
        name, phone = ctct
        print(f"{name} : {phone}")
    for name, phone in contacts.items():
        print(f"{name} : {phone}")


def addContact():
    global contacts
    print("ADD NEW CONTACT")
    print("---------------")
    fname = input("First Name: ").strip()
    lname = input("Last Name: ")
    lname = lname.strip()

    fullname = f"{lname},{fname}"

    # if fullname in contacts.keys():
    if fullname in contacts:
        print("CONTACT ALREADY THERE")
        return

    phone = input("Phone Number: ").strip()

    # ADD IT TO THE DICTIONARY
    contacts[fullname] = phone

    print(f"Added {fullname}")
    # pprint.pprint(contacts)
    # pprint(contacts)
    pp(contacts)


def updateContact():
    global contacts
    print("UPDATE CONTACT")
    print("---------------")
    fname = input("First Name: ").strip()
    lname = input("Last Name: ").strip()
    fullname = f"{lname},{fname}"

    # if fullname in contacts.keys():
    if fullname not in contacts:
        print("CONTACT AIN'T HERE YET")
        return

    phone = input("Phone Number: ").strip()

    # UPDATE IT IN THE DICTIONARY
    contacts[fullname] = phone

    print(f"Updated {fullname}")
    pp(contacts)


def deleteContact():
    global contacts
    print("DELETE CONTACT")
    print("---------------")
    fname = input("First Name: ").strip()
    lname = input("Last Name: ").strip()
    fullname = f"{lname},{fname}"

    # if fullname in contacts.keys():
    if fullname not in contacts:
        print("CONTACT AIN'T HERE YET")
        return

    # DELETE IT FROM THE DICTIONARY
    del contacts[fullname]

    print(f"Deleted {fullname}")
    pp(contacts)


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
        