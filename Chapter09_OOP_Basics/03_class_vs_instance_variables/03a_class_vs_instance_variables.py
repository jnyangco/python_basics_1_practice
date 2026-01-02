class Student:

    # CLASS VARIABLE
    # This belongs to the CLASS, not to any single object
    school_name = "ABC High School"
    total_students = 0

    def __init__(self, name, age):
        # INSTANCE VARIABLES
        # These belong to EACH object (student)
        self.name = name
        self.age = age
        Student.total_students += 1


def main():
    # Create two Student objects (instances)
    s1 = Student("Alice", 16)
    s2 = Student("Bob", 17)

    # Access INSTANCE VARIABLES (different per object)
    print(s1.name)
    print(s2.name)

    # Access CLASS VARIABLE
    # Both objects see the SAME value
    print(s1.school_name)
    print(s2.school_name)

    print("--------------------")
    # Change INSTANCE variable for s1 only
    s1.age = 20
    print(f"s1 age: {s1.age}")
    print(f"s2 age: {s2.age}")

    print("--------------------")

    # Change CLASS variable using the CLASS
    Student.school_name =  "XYZ International School"

    # Now ALL objects see the new value
    print(s1.school_name)
    print(s2.school_name)

    print("--------------------")
    print(f"Total Students: {Student.total_students}")

    print("--------------------")
    # NOTE: This is NOT usually used
    # Read class variables via objects -> BUT DO NOT Modify class variables via the class
    s1.school_name = "Private School"
    # should be -> School.school_name = "Private School"
    print(s1.school_name)
    print(s2.school_name)


if __name__ == "__main__":
    main()