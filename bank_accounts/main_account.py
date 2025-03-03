# Define the Account class
class Account:

    # Constructor to initialize account with person object and balance
    def __init__(self, person, balance):
        # The person associated with the account (instance of the Person class)
        self.person = person
        self.__balance = balance   # Private

    # Getter method to return the current balance
    def get_balance(self):
        return self.__balance

    # Method to deposit an amount into the account
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is: {self.__balance}")

    # Method to withdraw an amount from the account
    def withdraw(self, amount):
        # Check if there are sufficient funds to withdraw
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Your new balance is: {self.__balance}")
        else:
            # If there are insufficient funds, raise a custom exception
            raise InsufficientFundsException("Insufficient funds")

    # Method to return the account holder's full name
    def account_holder(self):
        # Calls the person's getter methods to get first and last names
        return f"{self.person.get_firstname()} {self.person.get_lastname()}"

    # Setter method for updating the account holder's last name
    def set_lastname(self, lastname):
        # Check if the provided last name is alphabetic (only letters allowed)
        if str(lastname).isalpha():
            self._lastname = lastname
        else:
            raise ValueError("Lastname must be alphabetic")

# Define a custom exception class for insufficient funds
class InsufficientFundsException(Exception):
    # Constructor to initialize the exception with a custom message
    def __init__(self, message):
        # Call the parent constructor to set the message
        super().__init__(message)






