# To replace all occurrences of 'a' with $ in a string

def rep_new_str(str1):
    new_str = ""
    for ch in str1:
        if ch == 'a':
            new_str += '$'
        else:
            new_str += ch

    return new_str

text = input("Enter New String: ")
print("New String is:", rep_new_str(text))
rep_new_str(text)