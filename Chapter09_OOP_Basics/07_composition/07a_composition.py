# Most modern frameworks use:
# Inheritance sparingly
# Composition heavily

# Instead of:
# class HomePage(BasePage):
#     ...

# You'll see:
# class HomePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WaitHelper(driver)

# Composition means:
# A class USES another class
# instead of BEING another class.

# Concept	Meaning	Example
# Inheritance ->	IS-A	-> HomePage -> IS-A BasePage
# Composition ->	HAS-A	-> HomePage -> HAS-A Driver

# ---------------------------------------------------------
# Why composition is important (especially for Selenium)
#
# In Selenium:
# A page HAS A:
# driver
# wait helper
# element helper
#
# A page is NOT a driver
# A page is NOT a wait
#
# So composition is often more natural than inheritance.


# ---------------------------------------------------------
# This class represents a component/helper
class Engine:
    def start(self):
        print("Engine started.")


# ---------------------------------------------------------
class Radio:
    def play_music(self):
        print("Playing music.")


# ---------------------------------------------------------
# This class USES Engine (HAS-A relationship)
class Car:
    def __init__(self):
        # COMPOSITION
        # Car HAS an Engine
        self.engine = Engine()  # -> THIS IS COMPOSITION
                                # CAR does NOT inherit from Engine
                                # CAR simply uses an Engine
        self.radio = Radio()    # -> COMPOSITION

    def drive(self):
        # Car uses the Engine object
        self.engine.start()
        print("Car is driving.")

        self.radio.play_music()


# ---------------------------------------------------------
def main():
    car = Car()
    car.drive()

if __name__ == "__main__":
    main()