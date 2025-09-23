def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


num = int(input("Enter a number: "))

sum_fact = 0    
for i in range(1, num + 1):
    sum_fact = sum_fact + fact(i)

print("Sum of Factorial of 1 to", num ," =", sum_fact)