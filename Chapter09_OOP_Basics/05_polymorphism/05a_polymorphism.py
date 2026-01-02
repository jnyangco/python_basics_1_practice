# PARENT CLASS
class Animal:

    def speak(self):
        # Generic behavior (can be overridden)
        print("The animal makes a sound.")


# -------------------------------------------------
# CHILD CLASS 1
class Dog(Animal):

    # OVERRIDE the speak() method
    def speak(self):
        print("The dog barks.")


# CHILD CLASS 2
class Cat(Animal):

    # OVERRIDE the speak() method
    def speak(self):
        print("The cat meows.")


# CHILD CLASS 3
class Cow(Animal):

    # OVERRIDE the speak() method
    def speak(self):
        print("The cow moos.")

# THIS IS POLYMORPHISM
# SAME CALL -> animal.speak() - BUT can be DIFFERENT BEHAVIOR depends on USAGE (runtime method selection)
def make_sound(animal):
    animal.speak()  # if you pass dog object -> it will be Dog.speak()

# -------------------------------------------------
def main():
    # Create objects of different classes
    animal = Animal()
    dog = Dog()
    cat = Cat()
    cow = Cow()

    # SAME method name, DIFFERENT behavior
    animal.speak()
    dog.speak()
    cat.speak()
    cow.speak()

    print("-----------------------")

    # Polymorphism through a list
    # LISTS OF OBJECTS/INSTANCE
    animals_list = [animal, dog, cat, cow]
    for a in animals_list:
        a.speak()

    print("-----------------------")
    make_sound(animal)
    make_sound(dog)
    make_sound(cat)
    make_sound(cow)


if __name__ == "__main__":
    main()