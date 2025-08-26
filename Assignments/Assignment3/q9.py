s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
s4 = int(input("Enter marks of subject 4: "))
s5 = int(input("Enter marks of subject 5: "))

avg = (s1 + s2 + s3 + s4 + s5) / 5

if (avg >= 80):
    print("First Class")
elif (avg >= 50):
    print ("Second Class")
elif (avg >= 35):
    print ("Third Class")
else:
    print("Fail")


