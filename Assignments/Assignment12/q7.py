# Calculate Length Of a string (Without len())

def string_length(s):
    count = 0
    for i in s:
        count += 1
    return count

s = input("Enter a String: ")
print("Length of string:", string_length(s))