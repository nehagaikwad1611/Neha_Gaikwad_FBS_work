num = int(input("Enter a number: "))
temp = num
s = 0

while(temp > 0):
    d = temp % 10
    fact = 1
    for i in range(1, d+1):
        fact = fact*i
    s = s + fact
    temp = temp // 10


if s == num:
    print(f'{num}: is a strong number')
else:
    print(f'{num}: is NOT a strong number')