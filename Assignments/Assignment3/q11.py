age = int(input("Enter Age: "))
ticket = float(input("Enter Ticket Price: "))

if age < 12:
    total = ticket - (ticket * 0.30)
elif age > 59:
    total = ticket - (ticket * 0.50)
else:
    total = ticket 

print(f'Total Ticket Amount: {total}')