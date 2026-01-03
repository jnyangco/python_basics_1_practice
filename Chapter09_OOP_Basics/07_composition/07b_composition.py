
# ---------------------------------------------------------
# This class represents a component/helper
class Engine:
    def start(self):
        print("Engine started.")



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
        self.engine.start()
        print("Car is driving.")


# ---------------------------------------------------------
def main():
    # Create an Engine object FIRST
    engine = Engine()

    # Inject the Engine into the Car
    car = Car(engine)

    # Use the car
    car.drive()

if __name__ == "__main__":
    main()