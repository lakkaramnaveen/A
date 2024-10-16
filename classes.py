class Car:
    def __init__(self, brand: str, horsepower: int ) -> None:
        self.brand = brand
        self.horsepower = horsepower

volvo: Car = Car('Volvo', 230)
