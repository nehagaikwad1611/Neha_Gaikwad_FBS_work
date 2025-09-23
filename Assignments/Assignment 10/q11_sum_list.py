# To find sum of all elements of list

def sum_list(list):
    total = 0
    for i in list:
        total += i
    return total

list = [10, 20, 30, 40, 50, 60]
print("Sum:", sum_list(list))