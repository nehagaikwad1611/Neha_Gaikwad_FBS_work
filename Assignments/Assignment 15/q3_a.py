class Shirt:
    def __init__(self, sid, sname, stype, price, size):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size


s1 = Shirt(301, "Formal Shirt", "Formal", 1200, "L")
print("Shirt object created successfully using constructor.")
