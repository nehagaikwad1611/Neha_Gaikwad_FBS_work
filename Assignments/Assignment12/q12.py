# Count number of lowercase characters

def count_lowercase(s):
    count = 0
    for ch in s:
        if 'a' <= ch <= 'z':
            count += 1
    return count 

s = input("Enter a string: ")
print("Lowercase characters:", count_lowercase(s))
    
