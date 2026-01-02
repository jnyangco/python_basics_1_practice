# class / blueprint
class Person:

    # Constructor
    def __init__(self, name, age):

        # Instance Variables - belongs to each object/instance object of this class
        self.name = name
        self.age = age


# This function is just to run our example code
def main():

    # Here we CREATE objects (also called INSTANCES) of the Person class

    # p1 is an object of type Person
    p1 = Person("Alice", 25)

    # p2 is an object of type Person
    p2 = Person("Bob", 30)

    p3 = Person("Charlie", 40)



    # Access instance variables using the object
    print(p1.name)  # Alice
    print(p1.age)   # 25

    print(p2.name)  # Bob
    print(p2.age)   # 30

    print(type(p1))
    print(type(p2))

    # PRACTICE
    print(p3.name)
    print(p3.age)


    print("-----------------------------")
    p1.age = 26
    print("After updating p1 age = 26")
    print(p1.name)
    print(p1.age)

    print("-----------------------------")
    # Store objects in list
    people = p1, p2, p3
    for person in people:
        print(person.name + " -> " + str(person.age))

    print("-----------------------------")
    # like a list of objects
    employees = [
        Person("Anna", 20),
        Person("Ben", 28),
        Person("Chris", 35)
    ]

    for employee in employees:
        print(employee.name + " -> " + str(employee.age))



if __name__ == "__main__":
    main()


