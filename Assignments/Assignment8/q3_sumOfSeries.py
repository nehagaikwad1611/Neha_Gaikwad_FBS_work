def add(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
        print(i, end =" ")
    return total 

num = int(input("Enter number: "))
print("Sum from 1 to", num,"=",add(num))
