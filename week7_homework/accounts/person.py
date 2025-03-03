# accounts/person.py

class InsufficientFundsException(Exception):
    """Custom exception for insufficient funds during withdrawal."""
    pass


class Person:
    def __init__(self, initial_amount, firstname, lastname, age, gender, email):
        self.__balance = initial_amount  # Private balance attribute
        self.firstname = firstname  # Public attribute
        self._lastname = lastname  # Protected attribute
        self._age = age
        self._gender = gender
        self._email = email

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money with error handling
    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsException(f"Insufficient funds! Available balance: ${self.__balance}")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Withdrawal amount must be positive.")

    def __str__(self):
        return f"{self.firstname} {self._lastname} is a {self._age}-year-old {self._gender} whose email address is {self._email}"
