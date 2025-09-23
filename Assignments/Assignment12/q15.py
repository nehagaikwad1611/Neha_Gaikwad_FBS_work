# To find larger string without using built- in functions.

# Take in two strings and display the larger string without using built in functions

def larger_string(s1, s2):
    len1, len2 = 0, 0
    for _ in s1:
        len1 += 1
    for _ in s2:
        len2 += 1
    if len1 >= len2:
        return s1
    else:
        return s2
    
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Larger String:", larger_string(s1,s2))