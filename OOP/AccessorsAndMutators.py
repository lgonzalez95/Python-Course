class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def area(self):
        return self.length * self.breadth


r = Rectangle(10, 8)
print(r.getLength())
r.setLength(8)
print(r.getLength())