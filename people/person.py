# Define the Person class
class Person:
    # Constructor to initialize a person's attributes
    def __init__(self, firstname, lastname, age, gender, email, address):
        self.__firstname = firstname  # Private
        self.__lastname = lastname    # Private
        self.__age = age              # Private
        self.__gender = gender        # Private
        self.__email = email          # Private
        self.__address = address      # Private

    # Getter method for the first name
    def get_firstname(self):
        return self.__firstname

    # Getter method for the last name
    def get_lastname(self):
        return self.__lastname

    # Getter method for the age
    def get_age(self):
        return self.__age

    # Getter method for the gender
    def get_gender(self):
        return self.__gender

    # Getter method for the email
    def get_email(self):
        return self.__email

    # Getter method for the address
    def get_address(self):
        return self.__address


