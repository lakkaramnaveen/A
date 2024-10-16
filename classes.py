class Car:
    def __init__(self, color: str, horsepower: int ) -> None:
        self.color = color
        self.horsepower = horsepower

volvo: Car = Car('red', 230)
print(volvo.color, volvo.horsepower)
