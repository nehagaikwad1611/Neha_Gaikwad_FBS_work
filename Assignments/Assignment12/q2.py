# Remove the nth index character

def remove_nth_char(s, n):
    result = " "
    for i in range(len(s)): # to go through each index i from 0  to len(s)-1
        if i != n:
            result += s[i]
    return result

s = input("Enter a String: ")
n = int(input("Enter index to remove: "))
print("After removing the nth index of character:", remove_nth_char(s, n))