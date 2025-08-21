area_wall = float(input("Enter area of one wall:"))
cost_interior = float(input("Enter cost for interior painting:"))
cost_exterior = float(input("Enter cost for exterior painting:"))

total_walls = 8 # 4 walls , 2 rooms

total_area = area_wall * total_walls

total_interior_cost = total_area * cost_interior
total_exterior_cost = total_area * cost_exterior

print(f'Total area :{total_area}')
print(f'Interior painting cost :{total_interior_cost}')
print(f'EXterior painting cost :{total_exterior_cost}')
