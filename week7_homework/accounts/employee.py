# accounts/employee.py
from accounts.person import Person  # Import the base class

class Employee(Person):
    def __init__(self, initial_amount, firstname, lastname, age, gender, email, employee_ID, job_position, job_department):
        # Call the Person constructor with required attributes
        super().__init__(initial_amount, firstname, lastname, age, gender, email)

        # Private attribute (cannot be accessed directly)
        self.__ID = employee_ID

        # Public attribute (can be accessed directly)
        self.position = job_position

        # Protected attribute (conventionally for internal use or subclasses)
        self._department = job_department

    # Getter for employee ID
    def get_employee_ID(self):
        return self.__ID

    # Getter for job position
    def get_job_position(self):
        return self.position

    # Getter for job department
    def get_job_department(self):
        return self._department

    # Override __str__() method to include employee details
    def __str__(self):
        return f"{self.get_firstname()} {self.get_lastname()} (Employee ID: {self.__ID}) works as a {self.position} in the {self._department} department."
