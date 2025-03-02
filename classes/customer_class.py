from person_class import Person
class Customer (Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)


    def __str__(self):
        person_info = super().__str__()
        return person_info, "\nBalance: " + str(self._balance) + "\nDeposit: " + str(self._deposit) + "\nWithdraw: " + str(self._withdraw)


customer = Customer("Liya", "Khan", "100", 100, 10)
print(customer)