class Car:
    def __init__(self, brand: str, horsepower: int ) -> None:
        self.brand = brand
        self.horsepower = horsepower

    # Dunder methods similar to toString method in java
    def __str__(self) -> str:
        return f'{self.brand}, {self.horsepower}hp'

volvo: Car = Car('Volvo', 230)
print(volvo)
