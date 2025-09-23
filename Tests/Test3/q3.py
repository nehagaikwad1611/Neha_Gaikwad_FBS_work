salary = int(input("Enter basic salary: "))
total = 0
for i in range(salary):
    if(salary <  20000):
        total_salary = salary*( 0.10 + 0.12 + 0.15)
    else:
        total_salary = salary*( 0.15 + 0.18 + 0.20)
print(f'Total salary of Employee:{salary}')