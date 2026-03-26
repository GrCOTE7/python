class Square:
    def __init__(self, length):
        self.l = length

    def perimeter(self):
        return 4 * (self.l)

    def area(self):
        return self.l * self.l


class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.r = radius

    def perimeter(self):
        return 2 * self.pi * self.r

    def area(self):
        return self.pi * self.r**2


# Initialize the classes
sqr = Square(10)
c1 = Circle(4)

print("Perimeter computed for Square: ", sqr.perimeter())
print("Area computed for Square: ", sqr.area())
print("\nPerimeter computed for Circle: ", round(c1.perimeter(), 2))
print("Area computed for Circle: ", round(c1.area(), 2))
