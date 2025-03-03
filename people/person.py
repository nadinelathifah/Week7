#   Person class (Base class)

# Person is the base class representing a general person with attributes: firstname, lastname etc.
# Attributes        are Variables (properties) associated with a class which stores data.
# Class             A blueprint/template for creating objects.
#                   It defines attributes (data) and methods (functions) that the objects will have.

# Object            An instance of a class.
#                   Objects have actual data and can perform actions.

# The __init__ constructor initializes the attributes of Person class when a Person object is created.
class Person:
    def __init__(self, firstname, lastname, age, gender, email, address):
        self.__firstname = firstname
        self._lastname = lastname
        self.__age = age
        self.__gender = gender
        self.__email = email
        self.__address = address

#   This method returns a string formatted output representation of the Person object.
#   It is called when you print or convert the object into a string.
    def __str__(self):
        return f"Name: {self.__firstname} {self._lastname}\nAge: {self.__age}\nGender: {self.__gender}\nEmail: {self.__email}\nAddress: {self.__address}"

#   SETTER
    def set_firstname(self, firstname):
        if str(firstname).isalpha():
            self.__firstname = firstname
        else:
            raise ValueError("First name must only contain alphabetic characters.")

    def set_lastname(self, lastname):
        if str(lastname).isalpha():
            self._lastname = lastname
        else:
            raise ValueError("Last name must only contain alphabetic characters.")

    def set_age(self, age):
        if age.is_integer():
            self.__age = age
        else:
            raise ValueError("Age must be an integer value.")

    def set_gender(self, gender):
        if str(gender).isalpha():
            self.__gender = gender
        else:
            raise ValueError("Gender must only contain alphabetic characters.")

    def set_email(self, email):
        if '@' not in email:
            raise ValueError("Please ensure you have entered a valid email address. Email must implement the following structure: username@domain")
        else:
            self.__email = email

    def set_address(self, address):
        self.__address = address


#   GETTER
    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self._lastname

    def get_fullname(self):
        return self.__firstname + " " + self._lastname

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def get_person_type(self):      #Polymorphism
        return f"Person Type: Person"












