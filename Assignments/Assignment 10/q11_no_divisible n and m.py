# Print numbers divible by m and n

def divisible_by_mn(list, m, n):
    result = []
    for i in list:
        if i % m == 0 and i % n == 0:
            result += [i]   # If true then added to the result
    return result

list = [13, 26, 39, 52, 65, 72, 60]
print("Divisible by 2 and 3=",divisible_by_mn(list, 2, 3 ))