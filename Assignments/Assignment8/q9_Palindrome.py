def checkPalindromeNo(num):
    for i in range(1,num):
        rev = (num % 10)* 100 + (num // 10 % 10)*10 +(num // 100)       
    return rev == num

num = int(input("Enter Number: "))
if checkPalindromeNo(num):
    print(f'{num} is a palindrome number.')
else:
    print(f'{num} is not a palindrome number')

   