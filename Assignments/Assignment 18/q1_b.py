class Complex:
    def __init__(self, real = 0, image = 0):
        self.real = real
        self.image = image

    def __del__(self):
        print("Object Destroyed")

c1 = Complex(2,3)
print("Complex Object Created")   
del c1