#   What is a Savings Account?

# A type of bank account that helps you save money while earning interest over time.
# Earning interest: The bank pays you a small percentage (interest) on the money you keep in the account.
#                   This is how your savings grow.

#   How does it work?
#   1) Deposit money into the account by: (a) depositing cash.
#                                         (b) transferring funds from another account.
#                                         (c) setting up direct deposits.

#   2) Interest: The bank pays interest based on the balance kept in the account.
#                Some banks pay interest in daily, monthly or annual basis.

#   3) Interest Compounding: you earn interest on the added amount.

# Withdrawal limit: limited to 6 times per month.

from accounts.account import Account
from people.person import Person, Employee, Customer

class Savings(Account):
    def __init__(self, account_holder, balance, savings_balance, interest):
        super().__init__(account_holder, balance)
        self.__savings_balance = savings_balance
        self.__interest = interest / 100

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




