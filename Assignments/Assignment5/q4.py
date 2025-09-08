num = int(input("Enter number: "))
temp = num
s = 0 #(s wi;; store the sum of digit)

# To count the digit
n = len(str(num)) # convert number to string = str and to count digit= len

while temp > 0:
    d = temp % 10 # gets the last digit of temp ex. 153 = 3
    s = s + (d ** n)
    temp = temp // 10 #remove the last digit from temp ex. 153 = 15

if s == num:
    print(f'{num}: is a Armstrong number')
else:
    print(f'{num}: is NOT a Armstrong number')
