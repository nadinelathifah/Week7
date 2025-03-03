# Import the Account class from the main_account module
from bank_accounts.main_account import Account

# Define the SavingsAccount class that inherits from the Account class
class SavingsAccount(Account):
    # Constructor to initialize a savings account with an initial balance
    def __init__(self, savingsbalance, interest_rate):
        # Private attribute to store the savings balance
        self.__savingsbalance = savingsbalance
        # Private attribute to store the interest rate
        self.__interest_rate = interest_rate

    # Getter method to return the current savings balance
    def get_balance(self):
        return self.__savingsbalance

    # Method to calculate and return the interest on the savings balance
    def calculate_interest(self):
        # The interest is calculated by multiplying the balance by the interest rate
        interest = self.__savingsbalance * self.__interest_rate
        return interest

    # Method to apply the interest to the savings balance
    def apply_interest(self):
        # Calculate the interest and add it to the current balance
        interest = self.calculate_interest()
        self.__savingsbalance += interest
        print(f"Interest of {interest} has been applied. New balance is: {self.__savingsbalance}")
