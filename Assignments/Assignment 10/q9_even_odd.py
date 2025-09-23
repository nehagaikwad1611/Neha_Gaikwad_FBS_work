# Write a program of having number of elements in the list and find out even and odd elements 
# in that list and then create two separate list which will have even elements and other will have odd elements

def even_odd(list):
    even = []
    odd = []
    for i in list:
        if i % 2 == 0:
            even += [i]
        else:
            odd += [i]
    return even , odd

n = int(input("Enter number of elements: "))
list = []

for i in range(n):
    ele = int(input("Enter elements: "))
    list += [ele]

ev, od = even_odd(list)
print("Even Numbers: ", ev)
print("Odd Numbers: ", od)
