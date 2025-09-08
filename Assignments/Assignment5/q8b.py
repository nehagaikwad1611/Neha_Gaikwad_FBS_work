n = int(input("Enter Number: "))
s = 0
for i in range(1, n+1):
    s = s +(n ** i)
print(f'Sum:{s}')