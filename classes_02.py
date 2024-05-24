class Dog:

    __kind = "canine"  # class variable shared by all instances here private

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance
        self.tooth = self.__kind

d = Dog("Fido")
e = Dog("Buddy")

print(d.tooth)  # shared by all dogs
print(e.tooth)  # shared by all dogs
print(d.name)   # unique to d
print(e.name)   # unique to e
