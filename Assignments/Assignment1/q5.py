P = int(input("Enter principle: "))
T = int(input("Enter Time(in years): "))
R = int(input("Enter Rate: "))

CP = P * ((1 + R / 100) ** T) - P
print(f'Compoud Interest : {CP}')