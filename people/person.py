#   Person class (Base class)
# Person is the base class representing a general person with attributes: firstname, lastname etc.

# Attributes            are variables (properties) associated with a class which stores data.
# Class                 A blueprint/template for creating objects.
#                       It defines attributes (data) and methods (functions) that the objects will have.

# Object                An instance of a class.
#                       Objects have actual data and can perform actions.

# The __init__ constructor initializes the attributes of Person class when an object is instantiated.
class Person:
    def __init__(self, firstname, lastname, age, gender, email, address):
        self.__firstname = firstname
        self._lastname = lastname
        self.__age = age
        self.__gender = gender
        self.__email = email
        self.__address = address


#   This __str__ is a special method defines how an object should be represented (as a string); it returns a string representation of the Person object.
#   It is called when you print the object.
    def __str__(self):
        return f"Name: {self.__firstname} {self._lastname}\nAge: {self.__age}\nGender: {self.__gender}\nEmail: {self.__email}\nAddress: {self.__address}"


#   SETTER
#   A setter is a method that allows you to modify the value of an attribute in an object.
#   setters validate the value of the data before it can be changed.
#   Alternatively, can be assigned by @{name of property}.setter like @firstname.setter.
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
#   A getter is a method that allows access to the value of an attribute in an object.
#   Here we are retrieving the value (data) of firstname (attribute) from instance object.
#   Specifically, it retrieves the data from a private or protected object attribute.
#   Alternatively, you could also instead use @property decorator to get the firstname.
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