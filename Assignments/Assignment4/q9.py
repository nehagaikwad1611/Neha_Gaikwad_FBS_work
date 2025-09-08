start = int(input("Enter start of range: "))
end = int(input("Enter end of range:"))
num = int(input("Enter number: "))
for i in range(start, end+1):
    if i % num == 0:
        print(i, end=" ")
print(f'Numbers are divisible by:{num} are')