l = float(input("Enter length of rectangle:"))
b = float(input("Enter breadth of rectangle:"))
r = float(input("Enter radius of semicircle:"))

area = (l * b) + (1/2 * 3.14 * r * r)
perimeter = 2 * (l + b) + (3.14 * r)
 
print(f'Area of figure:{area}')
print(f'perimeter of figure:{perimeter}')