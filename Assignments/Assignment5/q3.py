passengers = int(input("Enter number of passengers: "))
ticket = int(input("Enter ticket cost: "))
total = 0

for i in range(passengers):
    age = int(input("Enter age of passenger: "))
    if age < 12:
        total = total + (ticket* 0.7)
    elif age > 59:
         total = total + (ticket* 0.5)
    else:
        total = total + ticket

print(f'Total Ticket Amount:{total}')
