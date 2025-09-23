# Accept a no. from user and check if this ele is present in the list or not . Also tell how many times it is present in the list
def check_number(list, number):
    count = 0
    for ele in list:
        if ele == number:
            count += 1
    return count

list = [20, 30, 40, 50, 10, 90,10]
n = int(input("Enter number to check: "))
c = check_number(list,n)
if c > 0:
    print(f"{n} is present {c} times")
else:
    print(f"{n} is not present in list")
