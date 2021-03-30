# import pprint                   # import a module
# from pprint import pprint       # import a function from a module
from pprint import pprint as pp   # optionally give the function an alias
from contact import contact

# contacts = []
# contacts = ['alda,alan,5551212', 'barker,bob,5551313']

# contacts = {
#     'alda,alan': {
#         'fname': 'Alan',
#         'lname': "Alda",
#         'phone': '5551212',
#         'email': "alan@mash.gov"
#     }, 
#     'barker,bob': {
#         'fname': 'Bob',
#         'lname': "Barker",
#         'phone': '5551313',
#         'email': "bobby@priceisright.com"
#     }
# }

contacts = []

# aa = contact()
# aa.first_name = "Alan"
# aa.last_name = "Alda"
# aa.phone = "5551212"
# aa.email = "alan@mash.mil"

aa = contact("Alan", "Alda", "5551212", "alan@mash.mil")

# print(help(aa))

contacts.append(aa)

aa.set_email('alan@retired.dead')

aa.print_card()
# aa.__private()

for c in contacts:
    print(c)
    c.first_name = "BOOGER MAN"
    print(f"{c.get_first_name()} {c.get_last_name()}")
    c.say_hi("Bob")

# pp(contacts)

exit()






ctct = contacts['alda,alan']
pp(ctct)
print(ctct['email'])
print(f"Alan's email is {contacts['alda,alan']['email']}")

# exit()

def displayContacts():
    global contacts
    print("MY CONTACTS")
    print('-'*40)
    for key, ctct in contacts.items():
        # print(key)
        # print(ctct)
        name = ctct['fname'] + " " + ctct['lname']
        email = ctct['email']
        phone = ctct['phone']
        print(f"NAME:  {name}")
        print(f"EMAIL: {email}")
        print(f"PHONE: {phone}")
        print('-'*40)


def addContact():
    global contacts
    print("ADD NEW CONTACT")
    print("---------------")
    fname = input("First Name: ").strip()
    lname = input("Last Name: ")
    lname = lname.strip()

    fullname = f"{lname.lower()},{fname.lower()}"

    # if fullname in contacts.keys():
    if fullname in contacts:
        print("CONTACT ALREADY THERE")
        return

    phone = input("Phone Number: ").strip()
    email = input("Email Address: ").strip()

    # ADD IT TO THE DICTIONARY
    ctct = {}
    ctct['fname'] = fname
    ctct['lname'] = lname
    ctct['phone'] = phone
    ctct['email'] = email
    contacts[fullname] = ctct

    print(f"Added {fullname}")
    pp(contacts)


def updateContact():
    global contacts
    print("UPDATE CONTACT")
    print("---------------")
    fname = input("First Name: ").strip()
    lname = input("Last Name: ").strip()
    fullname = f"{lname.lower()},{fname.lower()}"

    # if fullname in contacts.keys():
    if fullname not in contacts:
        print("CONTACT AIN'T HERE YET")
        return

    ctct = contacts[fullname]
    
    # UPDATE PHONE IF (AND ONLY IF) USER TYPES IN AN UPDATE
    oldphone = ctct['phone']
    newphone = input(f"Phone Number ({oldphone}): ").strip()

    if len(newphone) > 0:
        ctct['phone'] = newphone

    # UPDATE EMAIL IF (AND ONLY IF) USER TYPES IN AN UPDATE
    oldemail = ctct['email']
    newemail = input(f"Email Address ({oldemail}): ").strip()

    if len(newemail) > 0:
        ctct['email'] = newemail
        

    # UPDATE IT IN THE DICTIONARY
    contacts[fullname] = ctct

    print(f"Updated {fullname}")
    pp(contacts)


def deleteContact():
    global contacts
    print("DELETE CONTACT")
    print("---------------")
    fname = input("First Name: ").strip()
    lname = input("Last Name: ").strip()
    fullname = f"{lname},{fname}".lower()

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
        