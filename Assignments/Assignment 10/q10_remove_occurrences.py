# Remove all occurrences of given element

def remove_occurrences(list, ele):
    res = []
    for i in list:
        if i != ele:
            res += [i]
    return res

list = [10, 20, 30, 40, 20, 40, 30]
print("Original List=",list)
print("New list=",remove_occurrences(list, 40))
    

