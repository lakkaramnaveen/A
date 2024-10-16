class Car:
    def __init__(self, brand: str, horsepower: int ) -> None:
        self.brand = brand
        self.horsepower = horsepower

volvo: Car = Car('Volvo', 230)
print(volvo.brand, volvo.horsepower)

bmw: Car = Car('BMW', 400)
print(bmw.brand, bmw.horsepower)
