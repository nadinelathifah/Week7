#   Person class (Base class)

# Person is the base class representing a general person with attributes: firstname, lastname etc.
# Attributes        are Variables (properties) associated with a class which stores data.
# Class             A blueprint/template for creating objects.
#                   It defines attributes (data) and methods (functions) that the objects will have.

# Object            An instance of a class.
#                   Objects have actual data and can perform actions.

# The __init__ constructor initializes the attributes of Person class when a Person object is created.
class Person:
    def __init__(self, firstname, lastname, age, email, address):
        self.__firstname = firstname
        self._lastname = lastname
        self.age = age
        self.__email = email
        self.__address = address

#   This method returns a string formatted output representation of the Person object.
#   It is called when you print or convert the object into a string.
    def __str__(self):
        return f"Name: {self.__firstname} {self._lastname}\nAge: {self.age}\nEmail: {self.__email}\nAddress: {self.__address}"

#   GETTER
    def get_person_type(self):      #Polymorphism
        return f"Person Type: Person"

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self._lastname

    def get_fullname(self):
        return self.__firstname + " " + self._lastname

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

#   SETTER
    def set_lastname(self, lastname):
        if str(lastname).isalpha():
            self._lastname = lastname
        else:
            raise ValueError("Last name must be alphabetic.")

    # def set_new_email(self):
    #     if



# Employee is a Subclass of Person and inherits the properties of Person while adding more attributes: employee_id, position.
class Employee(Person):
    def __init__(self, firstname, lastname, age, email, address, employee_id, position, salary):
#       super() is a function used to call a method from the base (super) class.
#       allows you to access the methods and properties of a base class
        super().__init__(firstname, lastname, age, email, address)
        self.__employee_id = employee_id
        self.position = position
        self.__salary = salary

    def display_info(self):
        person_info = super().__str__()
        return f"{person_info}\nEmployee ID: {self.__employee_id}\nPosition: {self.position}"

    def get_person_type(self):
        return f"Person Type: Employee"


#   Customer class (Subclass)
class Customer(Person):
    def __init__(self, firstname, lastname, age, email, address, customer_id, membership):
        super().__init__(firstname, lastname, age, email, address)
        self.__customer_id = customer_id
        self._membership = membership

    def display_info(self):
        person_info = super().__str__()
        return f"{person_info}\nCustomer ID: {self.__customer_id}\nMembership: {self._membership}"

    def get_person_type(self):
        return f"Person Type: Customer"


