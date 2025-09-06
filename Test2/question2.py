num = int(input("Enter three digit number: "))
d1 = num % 10
d2 =(num // 10) % 10
d3 = num // 100

if(d2 == 2*d1 and d3 == d1//2):
    print(f"Yes, you have done it.")
else:
    ("Please try next time")
