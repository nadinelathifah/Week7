from people.person import  Person
#   Customer class (Subclass)
class Customer(Person):
    customer_count = 0
    def __init__(self, firstname, lastname, age, gender, email, address, customer_id, membership):
        super().__init__(firstname, lastname, age, gender, email, address)
        self.__customer_id = customer_id
        self._membership = membership
        Customer.customer_count += 1

    def __repr__(self):
        return "\nCustomer iD: %s\nMembership: %s"%(self.__customer_id, self._membership)

    def __str__(self):
        person_info = super().__str__()
        return f"{person_info}\nCustomer ID: {self.__customer_id}\nMembership Type: {self._membership}"

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

#   GETTER

    def get_customer_id(self):
        return self.__customer_id

    def get_membership(self):
        return self._membership

    def get_person_type(self):
        return f"Person Type: Customer"