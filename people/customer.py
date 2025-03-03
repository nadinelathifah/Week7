from person import Person

class Customer(Person):

    def __init__(self, firstname, lastname, age, gender, email, address, customerid):
        # Call the parent (Person) constructor to initialize the common attributes
        super().__init__(firstname, lastname, age, gender, email, address)

        # Initialize employee-specific attributes
        self.__customerid = customerid  # Private




