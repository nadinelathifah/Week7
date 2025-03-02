# importing from person module to collect the code for first name and last name
from person_class import Person
# Employee class
# This can collect their employee details
# passing through person to inherit the name code
class Employee(Person):
    # creating a constructor in the class and passing through params like first name and last name to inherit this
    def __init__(self, firstname, lastname, idnumber, department):
        super().__init__(firstname, lastname)
        # new function to collect the employee's id number and department
        self._idnumber = idnumber
        self.department = department

    def __str__(self):
        person_info = super().__str__()
        return person_info + "\nEmployee ID: " + str(self._idnumber) + "\nDepartment: " + self.department


def main():
    employee = Employee("Liya", "Khan", "998833", "REPG")
    print(employee)

if __name__ == "__main__":
    main()