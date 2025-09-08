n = int(input("Enter number: "))
s = 0
fact = 1
for i in range(1,n):
    fact = fact*i
    s = s + fact
print(f'Sum:{s}')