from pprint import pprint as pp
from contact import contact

# contacts = {
#     'Barker,Bob': {
#         'fname': "Bob",
#         'lname': 'Barker',
#         'phone': '555-1212',
#         'email': 'bob@dope.com'
#     },
#     'Chaplain,Charlie': {
#         'fname': 'Charlie',
#         'lname': "Chaplain",
#         'phone': '555-1313',
#         'email': 'chuck@buck.muck'
#     }
# }

contacts = []

bb = contact("Bob", "Barker", '555-1212', 'bob@dope.com')

contacts.append(bb)

print(bb)
print(bb.get_phone())


exit()

cont = contacts["Chaplain,Charlie"]
pp(cont)

email = cont['email']
print(email)

print(contacts["Chaplain,Charlie"]['email'])

# exit()

def showcontacts():
    global contacts
    print("MY CONTACTS")
    print('-'*20)
    for key, contact in contacts.items():
        # print(key)
        # pp(contact)
        name = contact['fname'] + " " + contact['lname']
        phone = contact['phone']
        print(f"NAME:  {name}")
        print(f"EMAIL: {contact['email']}")
        print(f"PHONE: {phone}")
        print('-'*20)

def addcontact():
    global contacts
    print("NEW CONTACT")
    fname = input("First Name: ")
    fname = fname.strip()
    fname = fname.title()
    lname = input("Last Name: ")
    lname = lname.strip()
    lname = lname.title()
    
    fullname = f"{lname},{fname}"

    if fullname in contacts:
        print("ALREADY EXISTS!!!")
        return
    
    phone = input("Phone Number: ").strip()
    email = input("Email Address: ").strip()

    # create a dictionary
    cont = {}
    cont['fname'] = fname
    cont['lname'] = lname
    cont['email'] = email
    cont['phone'] = phone

    # ADD (CREATE) TO THE DICTIONARY
    pp(cont)
    contacts[fullname] = cont

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
    
    contact = contacts[fullname]

    oldphone = contact['phone']
    newphone = input(f"New Phone Number ({oldphone}): ").strip()

    if len(newphone) > 0:
        contact['phone'] = newphone

    oldemail = contact['email']
    newemail = input(f"New Email Address ({oldemail}): ").strip()

    if len(newemail) > 0:
        contact['email'] = newemail

    # UPDATE THE DICTIONARY
    contacts[fullname] = contact

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
