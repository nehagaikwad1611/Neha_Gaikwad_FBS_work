basic = int(input("Enter basic salary: "))

da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

total_salary = basic + da + ta + hra 
print(f'Total salary of Employee:{total_salary}')