class Shirt:
    size_prices = {
        "small":1.0,
        "medium": 1.1, 
        "large" : 1.2, 
        "xlarge": 1.3
    }

    def __init__(self, sid , sname , stype , price, size ):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price 
        self.size = size

    def finalPrice(self):
        if self.size in Shirt.size_prices:
            return self.price * Shirt.size_prices[self.size]
        else:
            return self.price
        
    def showShirt(self):
        data = f"SHIRT ID: {self.sid}\nNAME: {self.sname}\\nTYPE:{self.stype}\nPRICE: {self.price}\nSIZE:{self.size}"
        return data

s1 = Shirt(1, "Formal Shirt", "Formal", 1000, "Medium")
print(s1.showShirt())