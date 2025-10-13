class Shirt:
    def __init__(self, sid, sname, stype, price, size):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def ShowBook(self):
        print("Shirt Details:")
        print(f"ID: {self.sid}")
        print(f"Name: {self.sname}")
        print(f"Type: {self.stype}")
        print(f"Price: {self.price}")
        print(f"Size: {self.size}")


s1 = Shirt(303, "Party Wear", "Casual", 1500, "XL")
s1.ShowBook()
