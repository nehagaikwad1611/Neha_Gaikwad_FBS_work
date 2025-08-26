Gender = input("Enter gender(Male/Female):")
Age = int(input("Enter a age:"))
if( Gender == 'M'):
    if(Age >= 21):
        print(f"{Gender} is eligible for marriage.")  
    else:
        print(f"{Gender} is not eligible for marriage.")  
else:
    if(Age > 17):
        print(f"{Gender} is eligible for marriage.")  
    else:
        print(f"{Gender} is not eligible for marriage.")  

   
