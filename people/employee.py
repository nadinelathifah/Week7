from person import Person


class Employee(Person):
    # Initialize the Employee class with additional attributes
    def __init__(self, firstname, lastname, age, gender, email, address, employeeid, position, salary, department):
        # Call the parent (Person) constructor to initialize the common attributes
        super().__init__(firstname, lastname, age, gender, email, address)

        # Initialize employee-specific attributes
        self.__employeeid = employeeid  #Private
        self.position = position #Public
        self.__salary = salary  # Protected
        self.department = department #public

    # Getter method for the employee ID
    def get_employeeid(self):
        return self.__employeeid

    # Getter method for the salary
    def get_salary(self):
        return self.__salary

    def get_department(self):
        return self.department

    def set_employeeid(self,employeeid):
        self.__employeeid = employeeid

