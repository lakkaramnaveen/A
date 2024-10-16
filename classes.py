class Car:
    def __init__(self, brand: str, horsepower: int ) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def drive(self) -> None:
        print(f'{self.brand} is driving!!')

    def get_info(self) -> None:
        print(f'{self.brand} with {self.horsepower} horsepower !!')

volvo: Car = Car('Volvo', 230)
print(volvo.brand, volvo.horsepower)
volvo.get_info()
volvo.drive()
