# Joint Account:
#   Account shared between two or more individuals.
#   Shared between relatives, couples or business partners.
#   Functions like a standard account, checking or savings.
#   Allows anyone named in the account to access its funds.

from accounts.account import Account

class Joint(Account):
    def __init__(self, account_holders, balance):
        super().__init__(account_holders, balance)
        if len(account_holders) >= 2:
            self.account_holders = account_holders
        else:
            raise ValueError("A Joint Account must have at least 2 account holders")

    