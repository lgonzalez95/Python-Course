class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length * self.breadth)

    @staticmethod
    def is_square(length, breadth):
        return length == breadth

if __name__ == '__main__':
    r = Rectangle(10, 5)
    print(Rectangle.is_square(10, 5))
