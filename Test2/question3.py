import math

L = 50
B = 40
r = 20
rounds = 5
rate = 35

if L > 0 and B > 0 and r > 0:
    perimeter = (2 * L + B) + (3.14 * r)
    total_length = perimeter * rounds
    cost = total_length * rate
    print("Total cost of fencing : {cost}")
else:
    print("Invalid input!")