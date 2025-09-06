area_wall = float(input("Enter area of one wall:"))
cost_interior = float(input("Enter cost for interior painting:"))
cost_exterior = float(input("Enter cost for exterior painting:"))

total_walls = 8
total_area = area_wall * total_walls
walls = input("Enter Exterior , Interior or both:")
Int = input("Enter Int for Interior:")
Ext = input("Enter Ext for Exterior:")
B = ("Enter B for both:")

if(walls == Int):
    total_interior_cost = total_area * cost_interior
    print(f'Total cost for Interior:{Int}')
elif(walls == Ext):
    total_exterior_cost = total_area * cost_exterior
    print(f'Total cost for Exterior:{Ext}')
elif(walls == B):
    total_cost = total_area*( cost_interior + cost_exterior)
    print(f'Total cost for Both: {total_cost}')
else:
    print("Invalid choice")











