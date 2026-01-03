
# ---------------------------------------------------------
# This class represents a component/helper
class GasEngine:
    def start(self):
        print("Gas Engine started.")

# ---------------------------------------------------------
class ElectricEngine:
    def start(self):
        print("Electric Engine started.")



# ---------------------------------------------------------
# This class USES Engine (HAS-A relationship)
class Car:
    def __init__(self, engine):
        # COMPOSITION via INJECTION
        # Car DOES NOT create the engine
        # It RECEIVES an engine from outside
        self.engine = engine  # -> THIS IS COMPOSITION

    def drive(self):
        # Car uses the Engine object

        # Polymorphism-like behavior: different engines, same start() call
        self.engine.start()
        print("Car is driving.")


# ---------------------------------------------------------
def main():
    # Create an Engine object FIRST
    gas_engine = GasEngine()

    # Inject the Engine into the Car
    gas_car = Car(gas_engine)

    # Use the car
    gas_car.drive()


    print("------------------------")
    electric_engine = ElectricEngine()
    electric_car = Car(electric_engine)
    electric_car.drive()

if __name__ == "__main__":
    main()