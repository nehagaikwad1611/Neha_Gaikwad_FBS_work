class Product:
    discount = 40 # Static variable for discount percentage
    
    def __init__(self, pid = None, pname = None, price = 0, quantity =0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showDiscount():
        print(f"Current Discount : {Product.discount}%")

p1 = Product(1, "Laptop", 600000, 2)
Product.showDiscount()

