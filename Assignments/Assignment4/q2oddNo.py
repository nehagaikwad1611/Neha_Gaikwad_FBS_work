num = int(input("Enter number: "))
for i in range(1 , num):
    if num % 2 != 0:
        print(f'{num} is a odd number')
    else:
        print(f'{num} is a even number')