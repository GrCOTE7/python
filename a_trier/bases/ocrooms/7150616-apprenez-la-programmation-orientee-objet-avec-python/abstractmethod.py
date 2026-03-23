import abc  # permet de définir des classes de base


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2


s = Square(20)
print(s.area())

# ss = Shape()
# print(ss.area())
