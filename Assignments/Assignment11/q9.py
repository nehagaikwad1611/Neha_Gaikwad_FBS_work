# To create 3 lists of numbers, their squaeres and cubes

def num_sq_cube(list):
    n = 0
    for ele in list:
        n+=1
        sq = [0]*n
        cb = [0]*n

    for i in range(n):
        sq[i] = list[i] * list[i] 
        cb[i] = list[i] * list[i] * list[i]
    return list, sq, cb

list =[8, 16, 24, 9, 18, 20]
num, sq, cb = num_sq_cube(list)

print(f"NUMBERS:{num}")
print(f"SQUARE:{sq}")
print(f"CUBE:{sq}")




