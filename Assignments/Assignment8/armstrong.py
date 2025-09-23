def is_armstrong(num):
    temp = num 
    s = 0
    n = len(str(num))

    while temp > 0:
        d = temp % 10
        s = s + (d**n)
        temp //= 10

    return s == num

num = int(input("Enter number: "))
if is_armstrong(num):
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is NOT an armstron number")