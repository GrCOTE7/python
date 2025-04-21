class Drink:
    """Une boisson."""

    def __init__(self, price):
        """Initialise un prix."""
        self.price = price
        print("Price = ", price)

    def drink(self):
        """Boire la boisson."""
        print("Je ne sais pas ce que c'est, mais je le bois.")

class Coffee(Drink):
    """Café."""

    prices = {"simple": 1, "serré": 1, "allongé": 1.5}

    def __init__(self, type):
        """Initialise le type du café."""
        self.type = type
        print(type)
        super().__init__(price=self.prices.get(type, 1))

    def drink(self):
        """Boire le café."""
        print("Un bon café pour me réveiller !")

s = Coffee.drink("simple")
# print(Coffee.prices.items())
