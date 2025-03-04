#   Inheritance Hierarchy Exercise

#   Task A + B:
#       - Create a person inheritance hierarchy:
#       - Design 3 classes: person, employee and customer.
#       - Consider appropriate constructors, properties and methods for these classes.
#       - Demonstrate your understanding of encapsulation, inheritance and polymorphism.
#       - create a client script and instantiate objects based on the above classes and call their methods and set their properties to demonstrate working functionality.
#       - Create an Account inheritance hierarchy, as above, design one for bank account types + client script to demonstrate functionality.

from people.person import Person
from people.employee import Employee
from people.customer import Customer
from accounts.account import Account
from accounts.saving_account import Savings
from display import create_banner, add_border

print(create_banner("Welcome to Fairytale Bank", 95))

#   cinderella is an instance object created from the Person base class.
cinderella = Person("Princess",
                    "Cinderella",
                    19,
                    "Female",
                    "cinderella@gmail.com",
                    "9 Pumpkin Cottage Ln")

#   alice and hans are instance objects created from the Employee subclass.
alice = Employee("Alice",
                 "Liddell",
                 25,
                 "Female",
                 "alicerabbit@gmail.com",
                 "12 Wonderland Drive",
                 "E001",
                 "Accountant",
                 5000,
                 "Wonderland")

hans = Employee("Hans",
                "Westergaard",
                30,
                "Male",
                "princehans@gmail.com",
                "Frozen Palace",
                "E002",
                "Reception",
                200,
                "Wonderland")

#   snow is an instance object created from the Customer subclass.
snow = Customer("Snow",
                "White",
                20,
                "Female",
                "snow.white@gmail.com",
                "7 Dwarves St",
                "C001",
                "Silver")
print(add_border(0))

#   Displaying information from the instance object from Person base class:
print(cinderella)
print(cinderella.get_person_type())
print(add_border(0))

#   Displaying information from the instance object from Employee subclass:
print(alice.__repr__())
print(alice.get_person_type())
print(alice.get_employee_count())
print(add_border(0))
print(hans.__repr__())
print(hans.get_employee_count())
print(hans.set_employee_id("E002"))
print(add_border(0))
#   Displaying information from the instance object from Customer subclass:
print(snow.display_info())
print(snow.get_person_type())
print(add_border(90))
#   Changing Snow White's last name:
print(snow.set_lastname("Black"))
# Two ways to check:
print(snow.get_fullname())
print(snow.get_lastname())
print(add_border(90))


#   Setting up a Checking Account for Snow White
print(create_banner("Snow White Account", 97))
print("\n")
snow_account = Account(snow,0)
print(snow_account)

print(add_border(90))
#   Depositing $2100 into Snow White's account:
print(snow_account.deposit(2100))
print(snow_account.withdraw(100))

print(add_border(90))
#   Creating a savings account, depositing $1000 into the savings account and setting an interest rate:
snow_savings = Savings(snow, snow_account.get_balance(),0, 2.5)
print(snow_savings)

print(add_border(90))
print(snow_savings.deposit_to_savings(1000))
print(add_border(90))
print(snow_savings.add_interest())

# Problem: when main account balance is printed again, the $1000 transfer from main account -> savings account is not reflected in main account balance.

snow_withdraw = snow_savings.withdraw_savings(50)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(50)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(50)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(50)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(50)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(50)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(50)
print(snow_withdraw)

snow_count = snow_savings.get_withdrawal_attempts()
print(snow_count)



















