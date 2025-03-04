class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"\033[92m${amount} has been deposited to the account belonging to {self.account_holder.get_fullname()}.\033[0m\nNew balance: $\033[97m{self.__balance}\033[0m"
        else:
            return f"Invalid deposit. Please ensure that the deposited amount is a positive integer."

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            return f"\033[93m${amount} has been withdrawn from the account belonging to {self.account_holder.get_fullname()}.\033[0m\nNew balance: $\033[97m{self.__balance}\033[0m"
        else:
            raise InsufficientFundsException(f"Invalid withdrawal amount. Please enter a positive integer or check for sufficient funds.")

#   GETTER and SETTER
    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account holder: {self.account_holder.get_fullname()}\nCurrent balance: $\033[97m{self.__balance}\033[0m"


#   Define a custom exception class for insufficient funds:
class InsufficientFundsException(Exception):
#   Constructor to initialize the exception with a custom message.
    def __init__(self, message):
#   Call the parent constructor to set the message
        super().__init__(message)