from exceptions.insufficientfunds import InsufficientFundsException
from people.person import  Person
from accounts.account import Account
from items.item import Item
from tabulate import tabulate as tb
from date.date import Date

#   Customer class (Subclass)
class Customer(Person):
    customer_count = 0
    def __init__(self, firstname, lastname, age, gender, email, address, customer_id, membership, account = None, item = None):
        super().__init__(firstname, lastname, age, gender, email, address)
        self.__customer_id = customer_id
        self._membership = membership
        self.__account = account
        self.__item = item
        Customer.customer_count += 1

#   Returns python-readable format to display Customer class attributes only.
    def __repr__(self):
        return "\nCustomer iD: %s\nMembership: %s"%(self.__customer_id, self._membership)

    def __str__(self):
        person_info = super().__str__()
        return f"{person_info}\nCustomer ID: {self.__customer_id}\nMembership Type: {self._membership}"

    def make_purchase(self, item):
        total_cost = item.calculate_total_cost()
        if self.__account.get_balance() >= total_cost:
            self.__account.withdraw(total_cost)
        else:
            return InsufficientFundsException()


#   Using the tabulate module, create a list of lists to display the table like: | row | column | column |
#                                                                                | row | column | column |
    def display_receipt(self, item, date):
        data = [
            ["Customer Name", f"{self.get_fullname()}"],
            ["Customer ID", f"{self.__customer_id}"],
            ["Item Name", f"{item.get_item_name()}"],
            ["Item Cost", f"${item.get_item_cost()}"],
            ["Item Quantity", f"{item.get_item_quantity()}"],
            ["Total Cost", f"{item.calculate_total_cost()}"],
            ["Purchase Date", f"{Date.display_date(date)}"],
            ["Remaining Balance", f"${self.__account.get_balance()}"]
        ]
#       Display output in table format using tabulate (as tb)
        table = tb(data, headers=["Description","Details"], tablefmt="simple")

        top = "-----------------------------"
        middle = "          Receipt          "
        bottom = "-----------------------------"
        heading = f"{top}\n{middle}\n{bottom}"
        return f"{heading}\n{table}\n{bottom}"

#   SETTER
    def set_customer_id(self, customer_id):
        id_structure = f"C00{Customer.customer_count}"
        if customer_id == id_structure:
            self.__customer_id = customer_id
        else:
            raise ValueError("Customer ID must be in the following structure: C00{customer count}")

    def set_membership(self, membership):
        if str(membership).isalpha():
            self._membership = membership
        else:
            raise ValueError("Membership must only contain alphabetic characters.")

    def set_account(self, account):
        if isinstance(account, Account):
            self.__account = account

    def set_item(self, item):
        if isinstance(item, Item):
            self.__item = item
        else:
            raise ValueError("Item must be an object from Item class.")


#   GETTER
    def get_customer_id(self):
        return self.__customer_id

    def get_membership(self):
        return self._membership

    def get_account(self):
        return self.__account

    def get_item(self):
        return self.__item

    def get_person_type(self):
        return f"Person Type: Customer"

    @classmethod
    def get_customer_count(cls):
        return Customer.customer_count