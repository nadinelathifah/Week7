# accounts/customer.py
class Customer:
    def __init__(self, name, request, date):
        self.__name = name  # Private attribute (cannot be accessed directly)
        self.request = request  # Public attribute (can be accessed directly)
        self._date = date  # Protected attribute (conventionally for internal use)

    # Getter for customer name
    def get_name(self):
        return self.__name

    # Getter for request
    def get_request(self):
        return self.request

    # Getter for date
    def get_date(self):
        return self._date

    # Setter for date (allows controlled modification)
    def set_date(self, date):
        self._date = date

    # String representation for customer details
    def __str__(self):
        return f"Customer {self.__name} requested {self.request} on {self._date}."
