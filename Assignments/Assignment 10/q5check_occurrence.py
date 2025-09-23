def check_occurrence(list, num):
    count = 0
    for ele in list:
        if ele == num:
            count += 1
    return count

list = [20, 30, 40, 20, 50, 20]
n = int(input("Enter number to search: "))
count = check_occurrence(list, n)
if count > 0:
    print(n, "is present",count,"times")
else:
    print(n,"is not present")
    