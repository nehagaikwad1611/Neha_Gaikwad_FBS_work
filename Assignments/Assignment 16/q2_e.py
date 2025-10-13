class Product:
    discount = 40 # Static variable for discount percentage
    
    def __init__(self, pid , pname , price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def applyDiscount(self):
        discounted_price = self.price - (self.price * Product.discount / 100)
        return discounted_price

p1 = Product(1, "Laptop", 600000, 2)
print("Discounted Price:", p1.applyDiscount())

