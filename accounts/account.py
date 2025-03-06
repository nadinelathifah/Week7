# Account Base Class:
from exceptions.insufficientfunds import InsufficientFundsException

class Account:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"\033[92m${amount} has been deposited to the account belonging to {self.account_holder.get_fullname()}.\033[0m\nMain Account balance: $\033[97m{self.get_balance()}\033[0m"
        else:
            return ValueError("Ensure the deposit is a positive integer.")

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            return f"\033[93m${amount} has been withdrawn from the account belonging to {self.account_holder.get_fullname()}.\033[0m\nMain Account balance: $\033[97m{self.get_balance()}\033[0m"
        else:
            raise InsufficientFundsException()


#   GETTER
    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.account_holder

    def __str__(self):
        return f"Account holder: {self.account_holder.get_fullname()}\nCurrent balance: $\033[97m{self.get_balance()}\033[0m"