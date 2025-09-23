# To find the 2nd largest number in a list using bubble sort

def second_largest(list):
    n = len(list)

    #Bubble sort Descending order
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    #Now first ele is largest , second element is 2nd largest
    return list[0], list[1]

list = [20, 40, 60, 10, 80, 100, 50]
max_num, sec_max = second_largest(list)

print("Max Number is:", max_num)
print("Second Max Number:", sec_max)