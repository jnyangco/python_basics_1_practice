class Car:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


def main():
    car1 = Car("Toyota", "Red", 2020)
    car2 = Car("Honda", "Blue", 2022)
    car3 = Car("Mazda", "Yellow", 2023)

    print(car1.brand)
    print(car1.color)
    print(car1.year)

    print(car2.brand)
    print(car2.color)
    print(car2.year)

    print(type(car1))
    print(type(car2))

    print(car1.year > car2.year)

    print("-------------------------")
    car3.color = "White"
    print(car3.brand + " -> " + car3.color)

    print("-------------------------")
    cars = [car3, car2, car3]
    for car in cars:
        print(f"{car.brand} - {car.color} - {str(car.year)}")

if __name__ == "__main__":
    main()