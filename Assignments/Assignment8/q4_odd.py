def sum_odds(n):

    s = 0
    print("Odd numbers between 1 and ", n,":")    
    for i in range(1 , n+1):
        
        if i % 2 != 0:
            print(i) 
            s = s + i  
    print("sum of odd numbers = ",s)    
             
      
n = int(input("Enter n: "))  
sum_odds(n)