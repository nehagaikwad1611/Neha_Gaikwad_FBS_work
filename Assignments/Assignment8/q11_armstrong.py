def checkArmstrong(num):
    s = 0
    temp =num
    n = len(str(num))
    while temp > 0:
        d = temp % 10
        s = s + (d ** n)
        temp = temp // 10

    if s == num:
        print(num, "is an Armstrong Number")
    else:
        print(num, "is not an Armstrong Number")

n = int(input("Enter 3 digit number: "))
checkArmstrong(n)
