# Joint Account:
#   Account shared between two or more individuals.
#   Shared between relatives, couples or business partners.
#   Functions like a standard account, checking or savings.
#   Allows anyone named in the account to access its funds.
#   Does not merge individual accounts, but create a new one.

from accounts.account import Account
from people.person import Person


class Joint(Account):
    #   Constructor initialising two accounts where account_holder_1 overrides account_holder, and balance_1 overrides balance in Account base class.
    def __init__(self, account_holder_1, account_holder_2, balance_1, balance_2, joint_balance):
        super().__init__(account_holder_1, balance_1)
        self.account_holder_2 = account_holder_2
        self.__balance_2 = balance_2
        self.__joint_balance = joint_balance


    def deposit_to_joint(self):
        pass


#   SETTER
    def set_account_holder_1(self, account_holder_1):
        if isinstance(account_holder_1, Account):
            self.account_holder = account_holder_1

    def set_account_holder_2(self, account_holder_2):
        if isinstance(account_holder_2, Account):
            self.account_holder = account_holder_2

    def set_balance_1(self):
        return self.account_holder.get_balance()

    def set_balance_2(self):
        return self.account_holder_2.get_balance()


#   GETTER
    def get_joint_balance(self):
        return self.get_balance()


ariel = Person("Ariel",
                 "Triton",
                 35,
                 "Female",
                 "littlemermaid@gmail.com",
                 "6 Coral Seafoam Avenue")

triton = Person("King",
                  "Triton",
                  65,
                  "Male",
                  "7seas@gmail.com",
                  "6 Coral Seafoam Avenue")

ariel_account = Account(ariel, 25000)
triton_account = Account(triton, 705000)

print(ariel)
print("\n")
print(ariel_account)
print("\n")
print(triton)
print("\n")
print(triton_account)
print("\n")

joint = Joint(ariel_account, triton_account, 0, 0, 0)




