import math


class Polygon:
    def __init__(self, num_sides, *pol_sides):
        self.num_sides = num_sides
        self.sides = pol_sides[:num_sides]


class Triangle(Polygon):
    def __init__(self, num_sides, *triangle_sides):
        super().__init__(num_sides, *triangle_sides)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


t = Triangle(3, 10, 15, 9)
print(t.area())
