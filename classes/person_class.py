# Classes are like a 'blueprint' for creating objects
# in this task we need to create 3 classes for person, employee, and customer

# Person class:
# This can collect their first name and last name
class Person:
    # creating a constructor and passing through params like first name and last name to collect this
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return "First Name: " + self.firstname + "\nSecond Name: " + self.lastname


def main():
    person = Person("Alliyah", "Khan")
    print(person)

if __name__ == "__main__":
    main()