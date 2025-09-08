n = int(input("Enter number of students: "))
total_avg = 0

for i in range(1,n+1):
    total = 0
    print(f"Student", i)
    for j in range(1, 6):
        marks = int(input(f'Enter marks of subject {j}:'))
        total = total + marks
    perc = total / 5
    print(f'percentage:{perc}')
    total_avg = total_avg + perc
    print(f'Average percentage of students:{total_avg/n}')