class Shirt:
    def __init__(self, sid, sname, stype, price, size):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def __del__(self):
        print(f"Shirt object with ID {self.sid} destroyed.")


s1 = Shirt(302, "Casual Tee", "Casual", 500, "M")
del s1
