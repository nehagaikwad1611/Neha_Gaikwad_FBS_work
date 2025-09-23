def sum_prime(n):
    print("prime numbers between 2 and ", n,":")
    sum = 0
    
    for i in range(2, n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i, end = " ")
            sum = sum + i  
    
    print("sum of prime numbers = ",sum)    
              
n = int(input("Enter n: "))  
sum_prime(n)



