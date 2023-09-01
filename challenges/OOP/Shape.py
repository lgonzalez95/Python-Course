import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
        super().__init__('Rectangle')

    def area(self):
        return 'The rectangle area is ' + str(self.breath * self.length)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__('Circle')

    def area(self):
        return 'The circus area is ' + str(math.pi * (self.radius ** 2))


c = Circle(5)
r = Rectangle(2, 3)

print(c.area())
print(r.area())
