import random

userid = "digilocker"
password = "2345"

u = input("Enter User ID: ")
p = input("Enter password: ")

if(u == userid and p == password):
    num = random.randint(1000, 9999)
    print(f'Random number : {num}')
    check = int(input("Enter captcha: "))
    if (check == num):
        print("Login Successful.")
    else:
        print("Failed")
else:
    print("Invalid Password or User ID ")

