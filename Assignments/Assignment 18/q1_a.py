class Complex:
    def __init__(self, real = 0, image = 0):
        self.real = real
        self.image = image

c1 = Complex(2,3)
c2 = Complex(4,5)
print("Complex Numbers Created: ")
print(f"c1 = {c1.real} + {c1.image}i")
print(f"c1 = {c2.real} + {c2.image}i")