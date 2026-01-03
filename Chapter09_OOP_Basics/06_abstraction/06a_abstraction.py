# Topic 06: Abstraction (Forcing structure in OOP)
# Abstraction means:
# Hiding how something works
# While forcing what must exist

# In simple terms:
# A base class says:
# “If you inherit from me, you MUST implement these methods”
# The base class does not care how
# Child classes decide the details


# Why Abstraction matters (especially for Selenium)
# In a real framework:
# Every page must have:
# open()
# maybe is_loaded()
#
# But:
# A base page cannot know how each page opens
# So it forces a contract

# -------------------------------------------------------------
# ✅ Concept Check (Passed)
#
# You clearly understand:
#
# ✅ abstract base class = cannot instantiate
# ✅ abstract methods = must be implemented
# ✅ child classes fulfill the contract
# ✅ abstraction is about enforcing “what must exist”
# -------------------------------------------------------------


from abc import ABC, abstractmethod  # "ABC" means ABSTRACT

# -------------------------------------------------------------
### ABSTRACT BASE CLASS
# "ABC" means this tells python this CLASS is ABSTRACT
# You are NOT allowed to create Animal() directly
class Animal(ABC):
    """
    This is an ABSTRACT class.
    You CANNOT create objects directly from it.
    """

    # ABSTRACT METHOD 1 -> need to be implement by child class (Dog, Cat)
    # -> Every child class MUST implement speak()
    # if it doesn’t → Python raises an error
    # Sample Error -> TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'speak'
    @abstractmethod
    def speak(self):
        """
        Abstract method.
        Child classes MUST implement this method.
        """
        pass  # pass means: “No implementation here”
              # Python enforces subclasses to override it
              # note: pass can be just like ->
                # ...
                # raise NotImplementedError
                # """Subclasses must implement this"""

                # i.e:
                # @abstractmethod
                # def speak(self):
                #     ...

    # ABSTRACT METHOD 2 -> need to be implemented by child class (Dog, Cat)
    @abstractmethod
    def move(self):
        pass


# -------------------------------------------------------------
# CHILD CLASS 1
class Dog(Animal):
    # IF ONE OF THE ABSTRACT METHOD NOT IMPLEMENTED in CHILD CLASS -> IT WILL THROW AN ERROR
    def speak(self):
        print("The dog barks.")

    def move(self):
        print("The dog moves.")


# -------------------------------------------------------------
# CHILD CLASS 2
class Cat(Animal):

    def speak(self):
        print("The cat meows.")

    def move(self):
        print("The cat moves.")


# -------------------------------------------------------------
# CHILD CLASS 3
class Cow(Animal):

    def speak(self):
        print("The cow moos.")

    def move(self):
        print("The cow moves.")


# -------------------------------------------------------------
def main():
    dog = Dog()
    cat = Cat()

    dog.speak()
    cat.speak()

    # animal = Animal()
    # ERROR -> TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'speak'

    print("-----------------------------")
    dog.move()
    cat.move()

    print("-----------------------------")
    cow = Cow()
    cow.speak()
    cow.move()

if __name__ == "__main__":
    main()