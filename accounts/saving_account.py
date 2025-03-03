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
from people.person import Person, Employee, Customer

class Savings(Account):
    def __init__(self, account_holder, balance, savings_balance, interest):
        super().__init__(account_holder, balance)
        self.__savings_balance = savings_balance
        self.__interest = interest / 100
        self.withdrawal_attempts = 0


    def deposit_to_savings(self, amount):
        if 0 < amount < self.get_balance():
            self.__savings_balance += amount
            self.withdraw(amount)
            return f"\033[92m${amount} has been transferred to the savings account belonging to {self.account_holder}.\033[0m\nMain Account balance: $\033[97m{self.get_balance()}\033[0m\nSavings Account balance: $\033[97m{self.__savings_balance}\033[0m"
        else:
            return f"Invalid transfer. Ensure that the number you have entered is positive and that you have sufficient balance in your main account."


    def get_savings_balance(self):
        return self.__savings_balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nMain Account balance: $\033[97m{self.get_balance()}\033[0m\nSavings Account balance: $\033[97m{self.get_savings_balance()}\033[0m"

    def add_interest(self):
        interest = self.__savings_balance * self.__interest
        self.__savings_balance += interest
        return f"Interest rate applied: \033[96m{self.__interest * 100}%\033[0m\nInterest rate amount: $\033[97m{interest:.0f}\033[0m\nNew savings balance: $\033[97m{self.__savings_balance:.0f}\033[0m"


    def withdraw_savings(self, amount):
        if self.withdrawal_attempts >= 6:
            return f"\033[1;91m★ Withdrawal Blocked ★ Unfortunately, you have reached the maximum withdrawal limit for this month.\nPlease refer to your checking account for future transactions.\033[0m"
        elif 0 < amount <= self.__savings_balance:
            self.__savings_balance -= amount
            self.withdrawal_attempts += 1
            return f"\033[93m${amount} has been withdrawn from the account belonging to {self.account_holder}.\033[0m\nNew balance: $\033[97m{self.__savings_balance}\033[0m"
        else:
            return f"Invalid withdrawal amount. Please ensure that you have entered a positive integer and that there are sufficient funds in your account."

    def get_count(self):
        return f"Withdrawal attempt: {self.withdrawal_attempts}"

