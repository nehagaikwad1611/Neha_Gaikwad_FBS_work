# To find max and min element in a list
def max_min_list(li):
    max_num = li[0]
    min_num = li[0]
    for ele in li:
        if(ele > max_num):
            max_num = ele
        if (ele < min_num):
            min_num = ele
    return max_num, min_num

li = [20, 40, 60, 80, 10, 50]
print("Maximum Number and Minimum Number", max_min_list(li))