# product
# constructor

class Product:
    discount = 10 # Static variable for discount percentage
    
    def __init__(self, pid = None, pname = None, price = 0, quantity =0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        data = f"PRODUCT ID: {self.pid}\nPRODUCT NAME: {self.pname}\nPRICE: {self.price}\nQUANTITY: {self.quantity}"
        return data
    
p1 = Product(1, "Laptop", 600000, 2)
p2 = Product()
print(p1.showProduct())

