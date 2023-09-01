from Rectangle import Rectangle


class Cuboid(Rectangle):
    def __init__(self, height, length, breadth):
        self.height = height
        super().__init__(length, breadth)

    def volume(self):
        return self.length * self.breadth * self.height


c = Cuboid(10, 5, 3)
print(c.volume())
