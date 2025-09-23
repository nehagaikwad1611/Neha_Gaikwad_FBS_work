# Sum All the items in a dictionary

def sum_dict(d):
    total = 0
    for k in d:
        total += d[k]
    return total

d = {1:10, 2:20, 3:30, 4:40}
print("Sum of values:",sum_dict(d))
