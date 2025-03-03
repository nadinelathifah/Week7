# client_script.py
from accounts.person import Person, InsufficientFundsException

# Create a Person object with an initial balance of $1000
person1 = Person(1000, "Daphne", "Smith", 31, "Female", "daphnesmith@gmail.com")

print(person1)
print(f"Initial Balance: ${person1.get_balance()}\n")

# Test deposit
person1.deposit(500)  # Depositing $500

# Test withdrawal with sufficient funds
try:
    person1.withdraw(200)  # Withdrawing $200
except InsufficientFundsException as err:
    print(err)

# Test withdrawal with insufficient funds
try:
    person1.withdraw(2000)  # Attempting to withdraw $2000 (should fail)
except InsufficientFundsException as err:
    print(err)

# Display final balance
print(f"\nFinal Balance: ${person1.get_balance()}")


