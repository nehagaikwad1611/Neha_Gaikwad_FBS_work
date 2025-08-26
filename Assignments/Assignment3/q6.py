cp = int(input("Enter cost price:"))
sp = int(input("Enter selling price:"))
profit = sp - cp
loss = cp - sp

if (sp > cp):
    print(f'Profit {profit}')
elif(cp > sp):
    print(f'Loss {loss}')
else:
    print("No Profit and No Loss")