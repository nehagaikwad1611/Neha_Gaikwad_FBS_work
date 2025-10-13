class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity


p1 = Product(201, "Laptop", 55000, 10)
print("Product object created successfully using constructor.")
