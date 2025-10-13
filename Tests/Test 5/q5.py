def list_union(list1, list2):
    union_list = list1.copy()

    for item in list2:
        if item not in union_list:
            union_list.append(item)

    return union_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = list_union(list1, list2)
print("Union of two lists:", result)