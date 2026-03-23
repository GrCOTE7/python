class amazon:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(
            f"This is product and amazon class is invoked.\nThe name is {self.name}. This costs {self.price} rupees.\n"
        )


class flipkart:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(
            f"This is product and flipkart class is invoked.\nThe name is {self.name}. This costs {self.price} rupees.\n"
        )


AMZ = amazon("Iphone", 4)
FLP = flipkart("Iphone", 2.5)
for product1 in (AMZ, FLP):
    product1.info()
