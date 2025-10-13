#Find elements in a given set that are not in another set

def difference_set(set1, set2):
    result = []
    for i in set1:
        found = False
        for j in set2:
            if i == j:
                found = True
                break
        if not found:
            result.append(i)
    return result

s1 = [1, 2, 3, 4, 5]
s2 = [4, 5, 6, 7]
print("Elements in s1 not in s2:", difference_set(s1,s2))