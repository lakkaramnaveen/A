class Car:
    def __init__(self, color: str, horsepower: int ) -> None:
        self.color = color
        self.horsepower = horsepower

volvo: Car = Car('red', 230)
print(volvo.color, volvo.horsepower)

bmw: Car = Car('black', 400)
print(bmw.color, bmw.horsepower)
