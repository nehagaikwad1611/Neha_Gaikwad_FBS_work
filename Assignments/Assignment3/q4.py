a = int(input("Enter first angle:"))
b = int(input("Enter second angle:"))
c = int(input("Enter third angle:"))

if(a + b + c == 180):
    print(f'{a}, {b}, {c} form a valid Triangle')
else:
    print(f'{a}, {b}, {c} form an invalid Triangle')


