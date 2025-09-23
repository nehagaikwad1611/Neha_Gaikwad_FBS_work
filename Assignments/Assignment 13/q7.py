
def multiply_dict(d):
    result = 1
    for k in d:
        result *= d[k]
    return result

d = {1:1, 2:2, 3:3, 4:4}
print("Sum of values:",multiply_dict(d))