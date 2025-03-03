from bank_accounts.main_account import Account
from people.person import Person
from bank_accounts.savings_account import SavingsAccount

try:
    person1 = Person("John", "Doe", 30, "Male", "john.doe@example.com", "123 Main St.")
    account = Account(person1, 1000)
    print(account.get_balance())
    print(account.person.get_lastname())
    account.deposit(50)
    account.withdraw(80)
    print(account.account_holder())
    account.set_lastname("Smith")
    savings_account = SavingsAccount(1000, 0.05)
    print(savings_account.get_balance())
    interest = savings_account.calculate_interest()
    print(f"Calculated Interest: {interest}")
finally:
    print("Thank you for using our bank!")