class Product:
    def __init__(self, pid , pname , price , quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print(f"[Product object is destroyed]{self.pname}")
    
p1 = Product(1, "Laptop", 600000, 2)
del p1


