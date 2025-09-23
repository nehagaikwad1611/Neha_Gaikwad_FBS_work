# print list after removing even number

def remove_even(li):
    res = []
    for i in li:
        if i % 2 != 0:
            res += [i]
    return res

li = [12,21,36,48,33,60,77]
print("After removing even numbers:", remove_even(li))