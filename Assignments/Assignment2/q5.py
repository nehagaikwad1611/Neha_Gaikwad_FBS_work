cp = int(input("Enter cost price of book: "))
discount = int(input("Enter discount percentage: "))

discount_amount = (cp*discount)/100
print(f'Discount Amount: {discount_amount}')

sp = (cp - discount_amount)
print(f'Selling Price: {sp}')