# Remove characters at odd index values

def remove_odd_index(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]
    return result

s = input("Enter a string: ")
print("Modified string:", remove_odd_index(s))

# Python
# odd positions ( 1, 3, 5)
# Even positions (0, 2, 4)
# Ans = pto