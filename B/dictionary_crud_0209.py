contacts = {}

print(contacts)

# CRUD


# CREATE

contacts["Big Bird"] = "123-456-789101112"
print(contacts)
print(len(contacts))


# READ

phone = contacts["Big Bird"]
print(phone)
print(contacts["Big Bird"])
print(f"Big Bird is at {contacts['Big Bird']}")

# UPDATE

contacts["Big Bird"] = "800-BIG-BIRD"
# if key exists in dict, update it,
# otherwise, add it
print(contacts)
print(len(contacts))

contacts["Grover"] = "555-1212"
print(contacts)
print(len(contacts))

contacts["grover"] = "800-Grover1"
print(contacts)
print(len(contacts))


# DELETE

del contacts["grover"]
print(contacts)
print(len(contacts))

print(contacts.pop("Big Bird"))
print(contacts)
print(len(contacts))

