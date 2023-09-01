class Cuboid:
    count = 0

    def __init__(self, ln, b, h):
        print(id(self))
        self.length = ln
        self.breadth = b
        self.height = h
        Cuboid.count += 1

    def area(self):
        return self.length * self.breadth

    def total(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)

    def volume(self):
        return self.length * self.breadth * self.height

    @classmethod
    def print_instances(cls):
        print(Cuboid.count)


c = Cuboid(10, 5, 3)
d = Cuboid(10, 5, 3)
print(c.area())
print(c.total())
print(c.volume())
print(id(c))
Cuboid.print_instances()
c.print_instances()
d.print_instances()
