from people.person import Person
from people.customer import Customer
from people.employee import Employee
from accounts.account import Account, InsufficientFundsException
from accounts.saving_account import Savings
from display import create_banner, add_border


try:
    print(create_banner("Welcome to Fairytale Bank", 95))
    cinderella = Person("Princess",
                        "Cinderella",
                        19,
                        "Female",
                        "cinderella@gmail.com",
                        "9 Pumpkin Cottage Ln")

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
                    "5 Palace Boulevard",
                    "E002",
                    "Reception",
                    200,
                    "Wonderland")

    snow = Customer("Snow",
                    "White",
                    20,
                    "Female",
                    "snow.white@gmail.com",
                    "7 Dwarves St",
                    "C001",
                    "Silver")
    print(cinderella)
    print(cinderella.get_person_type())
    print(add_border(0))
    print(alice)
    print(alice.get_person_type())
    print(hans.employee_count)
    print(add_border(0))
    print(hans)
    print(hans.get_employee_count())
    print(add_border(0))
    print(snow)
    print(snow.get_person_type())
    print(add_border(90))
    print(snow.set_lastname("Blue"))
    print(snow.get_fullname())
    print(snow.get_lastname())
    print(add_border(90))
    print(create_banner("Snow White: Checking Account", 97))
    print("\n")
    snow_account = Account(snow, 0)
    print(snow_account)
    print(add_border(90))
    print(snow_account.deposit(2100))
    print(snow_account.withdraw(100))
    print(add_border(90))
    snow_savings = Savings(snow, snow_account.get_balance(), 0, 2.5)
    print(snow_savings)
    print(add_border(90))
    print(snow_savings.deposit_to_savings(1000))
    print(add_border(90))
    print(snow_savings.add_interest())
except FileNotFoundError as error:
    print("★★★★★★★★★★★★★★ EXCEPTION: FileNotFoundError ★★★★★★★★★★★★★★")
    print(f"The following file can not be found: {error.filename}. Please try another file")
except TypeError as error:
    print("★★★★★★★★★★★★★★ EXCEPTION: TypeError ★★★★★★★★★★★★★★")
    print("The following operation has been performed on an incorrect/unsupported object type.")
    print(error)
except ValueError as error:
    print("★★★★★★★★★★★★★★ EXCEPTION: ValueError ★★★★★★★★★★★★★★")
    print("The following operation cannot be performed as an inappropriate value has been assigned to a variable or passed to a function when called.")
    print(error)
except InsufficientFundsException as error:
    print("★★★★★★★★★★★★★★ EXCEPTION: InsufficientFundsException ★★★★★★★★★★★★★★")
    print("There are not enough funds to process this operation.")
    print(error)
except Exception as error:
    print("★★★★★★★★★★★★★★ EXCEPTION: All other Exceptions ★★★★★★★★★★★★★★")
    print("A general exception has been raised.")
    print(error)
finally:
    print("Continue bank program.")
