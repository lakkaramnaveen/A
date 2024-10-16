class Car:
    def __init__(self, brand: str, horsepower: int ) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def drive(self) -> None:
        print(f'{self.brand} is driving!!')

    def get_info(self, size: int) -> None:
        print(size)
        print(f'{self.brand} with {self.horsepower} horsepower !!')

volvo: Car = Car('Volvo', 230)
volvo.get_info(7)
volvo.drive()
