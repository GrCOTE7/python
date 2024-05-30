class Baseclass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Rectangle(Baseclass):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")

        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Baseclass):
    def __init__(self, base, height):
        super().__init__("Triangle")

        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


forms = (Rectangle(100, 70), Triangle(base=70, height=100))

for form in forms:
    print("\nThe shape is:", form)
    print("The area of shape is", form.area())
