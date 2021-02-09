phone_numbers = {}

# CRUD

# CREATE

phone_numbers["Big Bird"] = "123-456-789101112"

print(len(phone_numbers))

# if the key exists, change the value for that key
# else, add the value for that key


# READ

print(f"Big Bird's phone number is {phone_numbers['Big Bird']}")
phone_no = phone_numbers["Big Bird"]
print(f"Big Bird's phone number is {phone_no}")

# phone_numbers["grover"] = "706-555-1212"    # REMEMBER THAT DICTIONARIES ARE CASE SENSITIVE
phone_numbers["Grover"] = "706-555-1212"    # REMEMBER THAT DICTIONARIES ARE CASE SENSITIVE
print(len(phone_numbers))

phone_no = phone_numbers["Grover"]
print(f"Grover's phone number is {phone_no}")

# UPDATE

phone_numbers["Big Bird"] = "800-BIG-BIRD"
print(f"Big Bird's phone number is {phone_numbers['Big Bird']}")

print(len(phone_numbers))

phone_numbers["grover"] = "800-GROVER1"  # OOPS I ADDED A LOWERCASE Grover
print(f"Big Bird's phone number is {phone_numbers['Grover']}")
print(len(phone_numbers))


# DELETE

del phone_numbers["grover"]
print(len(phone_numbers))

phone_numbers["Big Bird"] = None
print(len(phone_numbers))

