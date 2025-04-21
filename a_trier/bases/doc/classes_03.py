class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


Fido = Dog("Fido")
Bud = Dog("Buddy")
Fido.add_trick("roll over")
Bud.add_trick("play dead")
Bud.add_trick("play always")
print(Fido.tricks)
print(Bud.tricks)
