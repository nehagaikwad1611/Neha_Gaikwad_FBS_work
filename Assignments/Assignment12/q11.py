# To replace Every blank space with hyphen

def space_to_hyphen(s):
    result = ""
    for ch in s:
        if ch == " ": # if it is a space
            result += "_" #Replace with hyphen
        else:
            result += ch # Keep the same char
    return result

s = input("Enter a string: ")
print("String after replacing spaces with hyphens:" , space_to_hyphen(s))