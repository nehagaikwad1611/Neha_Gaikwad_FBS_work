num = int(input("Enter number: "))
for i in range(2, num+1):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ")
print("Number are not divisible by 2 and 3")