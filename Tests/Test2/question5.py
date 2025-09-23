p1 = int(input("Enter the price of first product: "))
p2 = int(input("Enter the price of second product: "))
p3 = int(input("Enter the price of third product:  "))
p4 = int(input("Enter the price of fourth product: "))
p5 = int(input("Enter the price of fifth product: "))

total = p1 + p2 + p3 + p4 + p5

if total > 0:
    gst = 0.18*total
    final_total = total + gst
    print(f'total:{total}')
    print(f'GST 18%:{gst}')
    print(f'Total bill:{total}')
else:
    print("Enter valid prices")