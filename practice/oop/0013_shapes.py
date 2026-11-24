"""Practice #13: Shape classes and polymorphism (attempt 1)."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

    def __repr__(self):
        return f"{type(self).__name__}(area={self.area():.2f})"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    shapes = [Circle(8), Rectangle(5, 9)]
    # polymorphism: same call, different behaviour
    for s in sorted(shapes, key=lambda s: s.area()):
        print(s)
    assert Rectangle(5, 9).area() == 45
