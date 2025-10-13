class Shirt:

    def __init__(self, sid , sname , stype , price, size ):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price 
        self.size = size

    # def __del__(self):
    #     print(f"[Product object is destroyed]")

s1 = Shirt(1, "Formal Shirt", "Formal", 1000, "Medium")
del s1