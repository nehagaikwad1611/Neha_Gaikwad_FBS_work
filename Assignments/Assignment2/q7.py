num = int(input("Enter three digit number: "))

d1 = num % 10
num = d1 // 10

d2 = num % 10
num = d2 // 10

d3 = num % 10
num = d3 // 10

print(f'd1:{d1}, d2:{d2}, d3:{d3}')
print(f'Sum of three digit number:{d1 + d2 + d3}')