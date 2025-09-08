userid = "digilocker"
password = "3456"

u = input("Enter userid: ")
p = input("Enter password: ")

for i in range(3):
    if u == userid and p == password:
        print("Login successfull!")
        break
    else:
        print("Invalid Credentials, Try again.")
else:
    print("3 attempts over")