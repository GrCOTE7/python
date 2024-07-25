class BrandClass:
    def __init__(self, brand, name, price):
        self.brand = brand.title()
        self.name = name
        self.price = price

    def info(self):
        print(
            f"This is product of {self.brand}.\nThe name is {self.name}. This costs {self.price} rupees.\n"
        )

AMZ = BrandClass("amazon shop", "Iphone", 4)
FLP = BrandClass("flipkart", "Iphone", 2.5)

for product in (AMZ, FLP):
    product.info()
