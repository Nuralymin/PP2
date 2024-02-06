class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width
        self.area = self.length * self.width
