import logging
logging.basicConfig(level = logging.DEBUG)

class contact:
    # FIELDS (ATTRIBUTES / PROPERTIES ==> STATE)
    #  (double-underscore makes it private)
    __first_name = None
    __last_name = None
    __phone = None
    __email = None

    # CONSTRUCTOR (ctor)
    def __init__(self, fn, ln, em, ph):
        '''
        Create a new contact using:

        fn == first name
        ln == last name
        em == email
        ph == phone
        '''
        logging.debug("I'm in INIT")
        logging.info(f"Creating...{fn} {ln}")
        self.__first_name = fn
        self.__last_name = ln
        self.__phone = ph
        self.__email = em

    
    # Change the defult string representation of an object
    def __str__(self):
        return f"CONTACT: {self.__last_name}, {self.__first_name}"

    # Cool example method
    def say_hi(self, to):
        '''
        A method to say hi to someone.

        to == someone (a string)
        '''
        print(f"Hello, there {to}. My name is {self.__first_name}")

    def print_card(self):
        print(f"NAME: {self.__first_name} {self.__last_name}")
        print(f"EMAIL: {self.__email}")
        print(f"PHONE: {self.__phone}")

    # ACCESSORS AND MUTATORS
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    # For shoots and giggles we'll make names read-only

    def set_email(self, em):
        if type(em) != str:
            print("BAD")
            return
        self.__email = em

    def set_phone(self, ph):
        self.__phone = ph

    def __private(self):
        print("HELLO")

if __name__ == "__main__":
    print("TESTING 1..2..3")
    c = contact("Paul","York","paul@porkfamily.groc","123456789")
    assert "Paul" == c.get_first_name()
    assert "paul@porkfamily.groc" == c.get_email()
    c.set_email("paul@yorkfamily.com")
    assert "paul@yorkfamily.com" == c.get_email()


