class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    # INSTANCE METHODS
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

    def have_birthday(self):
        self.age += 1
        print(f"{self.name} just turned {self.age}.")

    def is_adult(self):
        return self.age >= 18




def main():
    p1 = Person("Alice", 20)
    p1.say_hello()
    p1.have_birthday()
    p1.say_hello()

    print(f"Adult?: {p1.is_adult()}")




if __name__ == "__main__":
    main()