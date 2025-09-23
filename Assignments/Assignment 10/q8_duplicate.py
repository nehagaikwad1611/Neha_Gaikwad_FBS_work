# To create a duplicate existing of an existing list

def duplicate_list(list):
    list2 = []
    for ele in list:
        list2 = list2 + [ele]
    return list2

list1 = [10, 20, 30, 40, 50]
list2 = list1
print("List1:", list1)
print("List2:", list2)