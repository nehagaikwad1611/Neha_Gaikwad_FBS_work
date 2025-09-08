a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))

if(a + b > c and b + c > a and c + a > b):
    print(f'{a}, {b}, {c} form a valid Triangle')
else:
    print(f'{a}, {b}, {c} form an invalid Triangle')


