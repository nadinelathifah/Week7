#   Inheritance Hierarchy Exercise

#   Task A + B:
#       - Create a person inheritance hierarchy:
#       - Design 3 classes: person, employee and customer.
#       - Consider appropriate constructors, properties and methods for these classes.
#       - Demonstrate your understanding of encapsulation, inheritance and polymorphism.
#       - create a client script and instantiate objects based on the above classes and call their methods and set their properties to demonstrate working functionality.
#       - Create an Account inheritance hierarchy, as above, design one for bank account types + client script to demonstrate functionality.

from people.person import Person
from people.customer import Customer
from people.employee import Employee
from accounts.account import Account
from accounts.saving_account import Savings
from banners.display import create_banner, add_border
from items.item import Item
from date.date import Date

print(create_banner("Welcome to Fairytale Bank", 95))

#   cinderella is an instance object created by calling the Person base class (instantiation).
cinderella = Person("Princess",
                    "Cinderella",
                    19,
                    "Female",
                    "cinderella@gmail.com",
                    "9 Pumpkin Cottage Ln")

#   alice and hans are instance objects created from the Employee subclass.
alice = Employee("Alice",
                 "Rabbit",
                 25,
                 "Female",
                 "alicerabbit@gmail.com",
                 "12 Wonderland Drive",
                 "E001",
                 "Accountant",
                 0,
                 "Wonderland")

hans = Employee("Hans",
                "Westergaard",
                30,
                "Male",
                "princehans@gmail.com",
                "5 Palace Boulevard",
                "E002",
                "Chairman",
                0,
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

#   Displaying information of instance object cinderella from Person base class:
print(cinderella)
print(cinderella.get_person_type())
print(add_border(0))

#   Displaying information of instance object alice from Employee subclass:
print(alice)
print(alice.get_person_type())
print(alice.employee_count)
print(add_border(0))

#   Displaying information of instance object hans from Employee subclass:
print(hans)
print(hans.get_employee_count())
print(add_border(0))

#   Displaying information of instance object snow from Customer subclass:
print(snow)
print(snow.get_person_type())
print(add_border(90))
#   Changing Snow White's last name:
snow.set_lastname("Blue")
# Two ways to check:
print(snow.get_fullname())
print(snow.get_lastname())
print(add_border(0))
print("\n")

#   Creating a Checking Account for Employee hans:
print(create_banner("Prince Hans: Checking Account", 96))
print("\n")
hans_account = Account(hans)
# Depositing to the current balance:
hans_account.deposit(100000)
print(hans_account)
print(add_border(90))

#   Adding Monthly Salary:
# 1) Set the hans_account object to account parameter from Employee class:
hans.set_account(hans_account)
# 2) Set the salary assigned by the bank:
hans.set_salary(10000)
# 3) Add the salary amount to han's bank account (adding to current balance):
print(hans.add_monthly_salary())
# See the added monthly salary reflected in hans's checking account:
print(hans_account)
print(add_border(90))

#   Giving hans Employee a pay raise:
hans.add_raise()
# See the pay raise (20% of current salary) reflected in hans's checking account:
print(hans_account)
print(add_border(0))
print("\n")


#   Creating a Checking Account for Customer Snow Blue:
print(create_banner("Snow Blue: Checking Account", 94))
print("\n")
snow_account = Account(snow)
print(snow_account)
snow.set_account(snow_account)

print(add_border(90))
#   Depositing $2100 into Snow Blue's account:
print(snow_account.deposit(2100))
#   Withdrawing $100 from Snow Blue's account
print(snow_account.withdraw(100))
print(add_border(90))

#   Making a purchase:
# 1) Instantiate an object from Item class called 'apple'.
apple = Item("Apple")
# 2) Set the cost and quantity of said apple Item:
apple.set_item_cost(5)
apple.set_item_quantity(4)
# 3) Set the apple object to item parameter in Customer class:
snow.set_item(apple)
# 4) Calculate the total cost of the items:
apple.calculate_total_cost()
# 5) Make the purchase (item.calculate_total_cost() has already been applied to the make_purchase(self) method):
snow.make_purchase(apple)
#   Purchase is reflected as a deduction in snow_account balance:
print(snow_account)

#   Set a date for her purchase:
date = Date(21,12,1937)
print(snow.display_receipt(apple, date))
print(add_border(90))
print("\n")


#   Creating a savings account for Snow Blue, depositing $1000 into the savings account and setting an interest rate:
print(create_banner("Snow Blue: Savings Account", 94))
print("\n")
snow_savings = Savings(snow, snow_account.get_balance())
print(snow_savings)

print(add_border(90))
print(snow_savings.deposit_to_savings(1000))
snow_savings.set_interest(2.5)
print(add_border(90))
print(snow_savings.calculate_interest())

snow_withdraw = snow_savings.withdraw_savings(100)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(100)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(100)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(100)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(100)
print(snow_withdraw)

snow_withdraw = snow_savings.withdraw_savings(100)
print(snow_withdraw)

# 7th Withdrawal Attempt
snow_withdraw = snow_savings.withdraw_savings(100)
print(snow_withdraw)

snow_count = snow_savings.get_withdrawal_attempts()
print(snow_count)
