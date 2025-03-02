#   Person class (Base class)

class Person:
    def __init__(self, firstname, lastname, age, address):
        self.firstname = firstname
        self._lastname = lastname
        self.age = age
        self._address = address

    def __str__(self):
        return f"Name: {self.firstname} {self._lastname}\nAge: {self.age}\nAddress: {self._address}"

    def get_person_type(self):
        return "Person"


#   Employee class (Subclass)
class Employee(Person):
    def __init__(self, firstname, lastname, age, address, employee_id, position):
        super().__init__(firstname, lastname, age, address)
        self.__employee_id = employee_id
        self.__position = position

    def __str__(self):
        person_info = super().__str__()
        return f"Name: {person_info}\nEmployee ID: {self.__employee_id}\nPosition: {self.__position}"

    def get_person_type(self):
        return "Employee"


#   Customer class (Subclass)
class Customer(Person):
    def __init__(self, firstname, lastname, age, address, customer_id, membership):
        super().__init__(firstname, lastname, age, address)
        self.__customer_id = customer_id
        self._membership = membership

    def __str__(self):
        person_info = super().__str__()
        return f"Name: {person_info}\nCustomer ID: {self.__customer_id}\nMembership: {self._membership}"

    def get_person_type(self):
        return "Customer"

class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount