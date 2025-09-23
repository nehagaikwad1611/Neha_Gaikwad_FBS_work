num = int(input("Enter three digit number: "))
d1 = num // 100
d2 =(num // 10) % 10
d3 = num % 10

if(d1 == 2*d2 and d1*2 == d3):
    print(f"Yes, you have done it.")
else:
    ("Please try next time")
