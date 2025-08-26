num = int(input("Enter three digit number: "))

d1 = num % 10
d2 =(num // 10) % 10
d3 = num // 100

reverse = (d1 * 100) + (d2 * 10) + (d3)

print(f'd1:{d1}, d2:{d2}, d3:{d3}')
print(f'Reversed number : {reverse}')

if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
