n = int(input("Enter a number:"))
s = 0
fact = 1
for i in range(1 , n+1):
    fact = 1
    for j in range(1 , i+1):
        fact= fact*j
    s = s + (i / fact)

print(f'Sum of factorial series upto n:{s}')


