from people.person import  Person
#   Customer class (Subclass)
class Customer(Person):
    def __init__(self, firstname, lastname, age, gender, email, address, customer_id, membership):
        super().__init__(firstname, lastname, age, gender, email, address)
        self.__customer_id = customer_id
        self._membership = membership

    def display_info(self):
        person_info = super().__str__()
        return f"{person_info}\nCustomer ID: {self.__customer_id}\nMembership: {self._membership}"

    def get_person_type(self):
        return f"Person Type: Customer"