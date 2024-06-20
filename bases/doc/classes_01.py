class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        self.sum = self.r + self.i

    def f(self, v=7):
        return "hello world", self.sum, v, "ok"


x = Complex(3.0, -4.5)
print(x.r, x.i, x.sum)

counter = 1
print("Boucle de counter: ")
while counter < 10:
    counter *= 2
    print(counter, end=" ")
del counter

print("\nNbre de valeurs: ", len(list(x.f())))
print(x.f(55))

y = Complex(2, 5)
print(y.r, y.i, y.sum)
print(y.f())
