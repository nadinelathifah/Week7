from people.person import  Person

# Employee is a Subclass of Person and inherits the properties of Person while adding more attributes: employee_id, position.
class Employee(Person):
    employee_count = 0
    def __init__(self, firstname, lastname, age, gender, email, address, employee_id, position, salary, city):
#       super() is a function used to call a method from the base (super) class.
#       allows you to access the methods and properties of a base class
        super().__init__(firstname, lastname, age, gender, email, address)
        self.__employee_id = employee_id
        self.position = position
        self.__salary = salary
        self.__city = city
        Employee.employee_count += 1

#   Convert into string
    def __str__(self):
        person_info = super().__str__()
        return f"{person_info}\nEmployee ID: {self.__employee_id}\nPosition: {self.position}\nSalary: {self.__salary}\nCity: {self.__city}"

#   Returns python-readable format to display Customer class attributes only.
#   Storing in memory
    def __repr__(self):
        return "\nEmployee iD: %s\nPosition: %s\nSalary: %s\nCity: %s"%(self.__employee_id, self.position, self.__salary, self.__city)

#   SETTER
    def set_employee_id(self, employee_id):
        id_structure = f"E00{Employee.employee_count}"
        if employee_id == id_structure:
            self.__employee_id = employee_id
        else:
            raise ValueError("Employee ID must be in the following structure: E00{employee count}.\nThe employee count can be found via get_employee_count()")

    def set_position(self, position):
        if str(position).isalpha():
            self.position = position
        else:
            raise ValueError("Position title must only contain alphabetic characters.")

    def set_salary(self, salary):
        if salary.is_integer():
            self.__salary = salary
        else:
            raise ValueError("Salary must be an integer value.")

    def set_city(self, city):
        if str(city).isalpha():
            self.__city = city
        else:
            raise ValueError("City name must must only contain alphabetic characters.")


# GETTER

    def get_employee_id(self):
        return self.__employee_id

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.__salary

    def get_city(self):
        return self.__city

#   CLASS METHOD
#   A class method is a method that is bound to the class instead of the instance of a class.
#   Reflected by first argument cls instead of self.
#   Used to operate on the class itself, not instance.
    @classmethod
    def get_employee_count(cls):
        return Employee.employee_count

    def get_person_type(self):          # Polymorphism
        return f"Person Type: Employee"