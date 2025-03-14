# Savings Account:
#   A type of bank account that saves money while earning interest over time.
#   The bank pays a small percentage (interest) on the balance you keep in the account, and it is compounding.
#   Deposit money into the account by: (a) depositing cash.
#                                      (b) transferring funds from another account.
#                                      (c) setting up direct deposits.
#   Some banks pay interest in daily, monthly or annual basis.
#   Two types of savings accounts: (1) Fixed-rate savings: rate remains the same for the entire term.
#                                  (2) Variable savings: fluctuate by year.
#   Withdrawal limit: limited to 6 times per month.

from accounts.account import Account
from exceptions.insufficientfunds import InsufficientFundsException
from exceptions.withdrawal_attempts import WithdrawalLimitException


class Savings(Account):
    withdrawal_attempts = 0
    def __init__(self, account_holder, balance, savings_balance = 0, interest = 0):
        super().__init__(account_holder, balance)
        self.__savings_balance = savings_balance
        self.__interest = interest

#   This method deposits an amount from the main account to the savings account.
    def deposit_to_savings(self, amount):
        if 0 < amount < self.get_balance():
            self.withdraw(amount)
            self.__savings_balance += amount
            return f"\033[92m${amount} has been transferred to the savings account belonging to {self.account_holder.get_fullname()}.\033[0m\nMain Account balance: $\033[97m{self.get_balance()}\033[0m\nSavings Account balance: $\033[97m{self.get_savings_balance()}\033[0m"
        else:
            raise InsufficientFundsException()

#   This method withdraws from the savings account, adding increments to every withdrawal attempt.
#   The conditional statement states that if the withdrawal attempt exceeds 6 (times), raise the following exception.
    def withdraw_savings(self, amount):
        if Savings.withdrawal_attempts >= 6:
            raise WithdrawalLimitException()
    #   Otherwise, if the amount is bigger than 0 but less than the balance, then withdraw from the savings account balance.
        elif 0 < amount <= self.__savings_balance:
            self.__savings_balance -= amount
            Savings.withdrawal_attempts += 1
            return f"\033[93m${amount} has been withdrawn from the account belonging to {self.account_holder.get_fullname()}.\033[0m\nSavings Account balance: $\033[97m{self.get_savings_balance()}\033[0m"
        else:
            raise InsufficientFundsException()


#   The isinstance() is a built-in function that is used to validate whether the instance object belongs to a specific class.
#   However, in this scenario, it is used to check if the data from interest attribute in the object is a float.
    def set_interest(self, interest):
        if isinstance(interest, float):
            self.__interest = interest
        else:
            raise ValueError("Interest rate must be a float.")

    def calculate_interest(self):
        interest = self.__savings_balance * (self.__interest / 100)
        self.__savings_balance += interest
        return f"Interest rate applied: \033[96m{self.__interest}%\033[0m\nInterest rate amount: $\033[97m{interest:.2f}\033[0m\nSavings Account balance: $\033[97m{self.get_savings_balance()}\033[0m"


#   GETTER
    def get_savings_balance(self):
        return self.__savings_balance

    def get_interest(self):
        return self.__interest

    @classmethod
    def get_withdrawal_attempts(cls):
        return f"Withdrawal attempt: {Savings.withdrawal_attempts}"

    def __str__(self):
        return f"Account Holder: {self.account_holder.get_fullname()}\nMain Account balance: $\033[97m{self.get_balance()}\033[0m\nSavings Account balance: $\033[97m{self.get_savings_balance()}\033[0m"

#   Exception for withdrawal limit.

