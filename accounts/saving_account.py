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

from accounts.account import Account, InsufficientFundsException


class Savings(Account):
    withdrawal_attempts = 0
    def __init__(self, account_holder, balance, savings_balance, interest):
        super().__init__(account_holder, balance)
        self.__savings_balance = savings_balance
        self.__interest = interest


    def deposit_to_savings(self, amount):
        if 0 < amount < self.get_balance():
            self.__savings_balance += amount
            self.withdraw(amount)
            return f"\033[92m${amount} has been transferred to the savings account belonging to {self.account_holder.get_fullname()}.\033[0m\nMain Account balance: $\033[97m{self.get_balance()}\033[0m\nSavings Account balance: $\033[97m{self.__savings_balance}\033[0m"
        else:
            raise InsufficientFundsException("Invalid transfer. Ensure that the number you have entered is positive and that you have sufficient balance in your main account.")


    def withdraw_savings(self, amount):
        if Savings.withdrawal_attempts >= 6:
            return f"\033[1;91m★ Withdrawal Blocked ★ Unfortunately, you have reached the maximum withdrawal limit for this month.\nPlease refer to your checking account for future transactions.\033[0m"
        elif 0 < amount <= self.__savings_balance:
            self.__savings_balance -= amount
            Savings.withdrawal_attempts += 1
            return f"\033[93m${amount} has been withdrawn from the account belonging to {self.account_holder.get_fullname()}.\033[0m\nSavings Account balance: $\033[97m{self.__savings_balance}\033[0m"
        else:
            return InsufficientFundsException("Invalid withdrawal amount. Please ensure that you have entered a positive integer and that there are sufficient funds in your account.")


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
        return f"Interest rate applied: \033[96m{self.__interest}%\033[0m\nInterest rate amount: $\033[97m{interest:.0f}\033[0m\nSavings Account balance: $\033[97m{self.__savings_balance:.0f}\033[0m"


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
