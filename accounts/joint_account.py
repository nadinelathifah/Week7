# Joint Account:
#   Account shared between two or more individuals.
#   Shared between relatives, couples or business partners.
#   Functions like a standard account, checking or savings.
#   Allows anyone named in the account to access its funds.
#   Does not merge individual accounts, but create a new one.

from accounts.account import Account, InsufficientFundsException
from people.customer import Customer


class Joint(Account):
    #   Constructor initialising two accounts where account_holder_1 overrides account_holder in Account base class.
    def __init__(self, account_holder_1, account_holder_2, balance, joint_balance):
        super().__init__(account_holder_1, balance)
        self.account_holder_2 = account_holder_2
        self.__joint_balance = joint_balance


ariel = Customer("Ariel",
                 "Triton",
                 35,
                 "Female",
                 "littlemermaid@gmail.com",
                 "6 Coral Seafoam Avenue",
                 "C002",
                 "Platinum")

triton = Customer("King",
                  "Triton",
                  65,
                  "Male",
                  "7seas@gmail.com",
                  "6 Coral Seafoam Avenue",
                  "C003",
                  "Platinum")

ariel_account = Account(ariel, 25000)
triton_account = Account(triton, 705000)

print(ariel)
print("\n")
print(ariel_account)
print("\n")
print(triton)
print("\n")
print(triton_account)

joint = Joint(ariel_account, triton_account, 0, 0)