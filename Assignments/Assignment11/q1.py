# Python program to put even and odd elements of a list into 2 different lists

def seperate_even_odd(list):
    even = []
    odd = []

    for i in list:
        if i % 2 == 0:
            even+=[i]
        else:
            odd+=[i]
    return even,odd
list = [20,99,90,88,77,65,84,89]
ev,od = seperate_even_odd(list)  
print("Even no: ", ev)   
print("Odd no: ", od)   
   
