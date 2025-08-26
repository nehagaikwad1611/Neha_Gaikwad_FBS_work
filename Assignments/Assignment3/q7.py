userid = "digilocker"
password = "2345"

u = input("Enter User ID: ")
p = input("Enter password: ")

if(u == userid and p == password):
    print("Login successful.")
else:
    print("Invalid Password or User ID ")