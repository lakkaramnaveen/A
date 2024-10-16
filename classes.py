from typing import Self


class Car:
    def __init__(self, brand: str, horsepower: int ) -> None:
        self.brand = brand
        self.horsepower = horsepower

    # Dunder methods similar to toString method in java
    def __str__(self) -> str:
        return f'{self.brand}, {self.horsepower}hp'

    def __add__(self, other: Self) -> str:
        return f'{self.brand} & {other.brand}'


volvo: Car = Car('Volvo', 230)
bmw: Car = Car('BMW', 230)

print(volvo)
print(volvo.__add__(bmw))
