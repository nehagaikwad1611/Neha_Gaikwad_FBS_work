# Remove Intersection Of a second set with a first set

def remove_intersection(set1, set2):
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
s2 = [3, 4, 6]
print("After removing intersection:", remove_intersection(s1, s2))
