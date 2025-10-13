class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def ShowBook(self):
        print("Product Details:")
        print(f"ID: {self.pid}")
        print(f"Name: {self.pname}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

p1 = Product(203, "Keyboard", 1200, 30)
p1.ShowBook()
