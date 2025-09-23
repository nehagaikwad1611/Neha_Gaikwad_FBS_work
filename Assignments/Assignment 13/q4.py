def generate_square_dict(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i * i
    return d

print("Generted Dictionary:", generate_square_dict(10))