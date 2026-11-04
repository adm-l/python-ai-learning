class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = float(value)


class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    temperature = Temperature(21)
    print("temperature:", temperature.celsius)
    try:
        temperature.celsius = -300
    except ValueError as exc:
        print("validation:", exc)

    point = Point(2, 4)
    print("point:", point.x, point.y)
    try:
        point.label = "origin"
    except AttributeError as exc:
        print("slots prevent extra attribute:", type(exc).__name__)
