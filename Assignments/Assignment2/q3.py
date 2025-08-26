feet = int(input("Enter distance in feet: "))
inch = int(input("Enter distance in inches: "))

total_inches = (feet*12) + inch
cm = total_inches * 2.54
meter = cm / 100

print(f'Total distance in Meter:{meter}')
print(f'Total distance in Centimeter:{cm}')
