def print_pattern(n):
    for i in range(n): 
        print("*", end = " ")
    print()

    for i in range(1, n-1):
        for j in range(n-i-1):
            print(" ", end = " ")
        print("*")

    for i in range(n):
        print("*", end = " ")
    print()

size = int(input("Enter size: "))
print_pattern(size)