ticket = float(input("Enter Ticket Price: "))
total_amount = 0.0

print("\nPerson 1:")
age1 = int(input("Enter Age: "))

if age1 < 12:
    total1 = ticket - (ticket * 0.30)
elif age1 > 59:
    total1 = ticket - (ticket * 0.50)
else:
    total1 = ticket
total_amount += total1

print("\nPerson 2:")
age2 = int(input("Enter Age: "))

if age2 < 12:
    total2 = ticket - (ticket * 0.30)
elif age2 > 59:
    total2 = ticket - (ticket * 0.50)
else:
    total2 = ticket
total_amount += total2

print("\nPerson 3:")
age3 = int(input("Enter Age: "))

if age3 < 12:
    total3 = ticket - (ticket * 0.30)
elif age3 > 59:
    total3 = ticket - (ticket * 0.50)
else:
    total3 = ticket
total_amount += total3

print("\nPerson 4:")
age1 = int(input("Enter Age: "))

if age1 < 12:
    total4 = ticket - (ticket * 0.30)
elif age1 > 59:
    total4 = ticket - (ticket * 0.50)
else:
    total4 = ticket
total_amount += total4

print("\nPerson 5:")
age1 = int(input("Enter Age: "))

if age1 < 12:
    total5 = ticket - (ticket * 0.30)
elif age1 > 59:
    total5 = ticket - (ticket * 0.50)
else:
    total5 = ticket
total_amount += total5

print(f'Total amount for all 5 perosons:{total_amount}')