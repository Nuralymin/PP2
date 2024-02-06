class Shape:
    def __init__(self, length=0):
        self.length = length
        self.area = 0

    def printArea(self):
        print(f"Area of the shape: {self.area}")

class Square(Shape):
    def __init__(self, side):
        super().__init__(side)
        self.area = self.length * self.length