class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print(f"Product object with ID {self.pid} destroyed.")


p1 = Product(202, "Mouse", 800, 50)
del p1
