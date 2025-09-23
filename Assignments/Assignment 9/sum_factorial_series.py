#write a program to find sum of following series using recursive functions:
#1! + 2! + 3!+---

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1) # n! = n* (n-1)

def sum_series(n):
    if n == 0:
        return 0
    return fact(n) + sum_series(n-1)

n = int(input("Enter n: "))
print("Sum of series:", sum_series(n))