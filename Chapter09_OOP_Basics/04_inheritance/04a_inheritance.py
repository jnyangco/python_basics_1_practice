# PARENT CLASS (Base / Super class)
class Animal:

    # CONSTRUCTOR of the parent class
    def __init__(self, name):
    # INSTANCE METHOD in parent class
        self.name = name

    # INSTANCE METHOD in parent class
    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping")



# --------------------------------------------------------------------
# CHILD CLASS (Derived / Sub class)
# Dog INHERITS from Animal
class Dog(Animal):

    # CONSTRUCTOR of the child class
    def __init__(self, name, breed):
        # Call the PARENT class constructor
        super().__init__(name)

        # Child-specific instance variable
        self.breed = breed

    # Override parent method - dog has its own version of eat()
    # Python uses the Child version first
    def eat(self):
        print(f"{self.name} is eating dog food.")

    # Child-specific instance method
    def bark(self):
        print(f"{self.name} is barking.")



# --------------------------------------------------------------------
# Exercise - another CHILD class Cat
class Cat(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def meow(self):
        print(f"{self.name} is meowing.")



# --------------------------------------------------------------------
def main():
    # Create a Dog object
    dog = Dog("Buddy", "Golden Retriever")

    # Call method from PARENT class
    dog.eat()

    # Call method from CHILD class
    dog.bark()

    # Call method from PARENT class (Dog class -> Parent class)
    dog.sleep()

    # Access instance variables
    print(f"Name: {dog.name}")
    print(f"Breed: {dog.breed}")

    print("--------------------------")
    cat = Cat("Kitty", "Fluffy")
    cat.eat()
    cat.meow()
    print(f"Name: {cat.name}")
    print(f"Breed: {cat.breed}")



if __name__ == "__main__":
    main()