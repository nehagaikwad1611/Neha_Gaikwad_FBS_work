class Shirt:

    def __init__(self, sid , sname , stype, price, size ):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price 
        self.size = size

    def showShirt(self):
        data = f"SHIRT ID: {self.sid}\nNAME : {self.sname}\nTYPE:{self.stype}\nPRICE: {self.price}\nSIZE:{self.size}"
        return data
    
s1 = Shirt(1, "Formal Shirt", "Formal", 1000, "Medium")
print(s1.showShirt())