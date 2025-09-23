length = float(input("Enter length of one wall:"))
height = float(input("Enter height of one wall:"))
rate = float(input("Enter painting rate :"))

area_one_wall = length * height
total_area = 4 * area_one_wall

if total_area > 0 and rate >= 0:
    total_cost = total_area * rate
    print(f"Total area = {total_area:}")
    print(f"Total cost = {total_area:}")
else:
    print("Enter valid measurements")








