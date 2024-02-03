class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = float(input())
    def area(self):
        return self.length**2

x = Square()
print(x.area())
y = Shape()
print(y.area())
            