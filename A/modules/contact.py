import logging

# set the logging threshold level
#  NORMALLY you control this with an argument
# logging.basicConfig(level = logging.DEBUG)

class contact:
    # __ "protects" a field (effective "private")
    __first_name = None
    __last_name = None
    __phone = None
    __email = None
    __age = 0

    # CONSTRUCTOR (INITIALIZER)
    # def __init__(self):
    def __init__(self, fname, lname, ph, em):
        '''
        Create a new contact.

        parms:
          fname -- first name
          lname -- last name
          ph -- phone number
          em -- email address 
        '''
        logging.debug("In Init")
        logging.debug(f"{fname}, {lname}, {ph}, {em}")

        # Set the initial state
        self.__first_name = fname
        self.__last_name = lname
        self.__phone = ph
        self.__email = em


    def __str__(self):
        # return "DOH!"
        return f"{self.__last_name}, {self.__first_name}"

    
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_fname):
        self.__first_name = new_fname
    
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, new_lname):
        self.__last_name = new_lname
    
    def get_phone(self):
        return self.__phone

    def set_phone(self, new_phone):
        self.__phone = new_phone
    
    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        self.__age = new_age

    def happy_birthday(self):
        currage = self.__age
        self.__age += 1
        print(f"CONGRATS ON TURNING FROM {currage} TO {self.__age}")


#  UNIT TESTING USING ASSERTIONS
if __name__ == "__main__":
    c = contact("Paul", "York", "555-9999", "paul@yorkfamily.com")
    assert c.get_first_name() == "Paul"
    assert c.get_last_name() == "York"
    c.set_age(47)
    assert c.get_age() == 47
    c.happy_birthday()
    assert c.get_age() == 48
