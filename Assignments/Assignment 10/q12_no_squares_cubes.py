#To create three lists of number, their squares and cubes

def num_sq_cube(li):
    n = 0
    for ele in li:
        n += 1
    sq = [0]*n
    cb = [0]*n

    for i in range(n):
        sq[i] = li[i] * li[i]
        cb[i] = li[i] * li[i]* li[i]
    return li, sq, cb

li = [8, 16, 7, 14, 4]
num, sq, cb = num_sq_cube(li)

print(f"NUMBERS: {num}")
print(f"SQUARE: {sq}")
print(f"CUBE: {cb}")