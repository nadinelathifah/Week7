#   Inheritance Hierarchy Exercise

#   Task A + B:
#       - Create a person inheritance hierarchy:
#       - Design 3 classes: person, employee and customer.
#       - Consider appropriate constructors, properties and methods for these classes.
#       - Demonstrate your understanding of encapsulation, inheritance and polymorphism.
#       - create a client script and instantiate objects based on the above classes and call their methods and set their properties to demonstrate working functionality.
#       - Create an Account inheritance hierarchy, as above, design one for bank account types + client script to demonstrate functionality.

from accounts.account import Person, Employee, Customer

alice_employee = Employee("Alice", "Smith", 25, "123 Main St", "E001", "Analyst")
brian_customer = Customer("Brian", "Johnson",45, "456 Main St", "C001", "Normal")

print()
print(alice_employee.__str__())
print(alice_employee.get_person_type())

print(brian_customer.__str__())
print(brian_customer.get_person_type())
