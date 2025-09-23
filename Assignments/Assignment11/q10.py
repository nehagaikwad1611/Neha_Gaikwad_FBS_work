# to print list after removing even numbers

def remove_even(li):
    res = []
    for i in li:
       if  i % 2 != 0:
          res += [i]
    return res

li = [15, 12, 20, 24, 29, 11, 68]
print("After removing even numbers:" , remove_even(li))
