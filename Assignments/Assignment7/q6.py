for i in range(1, 6):
    for j in range(1, 6):
        if(i == 1 or i == j or j == 5 ):
            print(j, end=" ")
        else:
            print("", end="")   
    print()
