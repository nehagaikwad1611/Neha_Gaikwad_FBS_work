# Exchange first and last character

def swap_first_last(s):
    if len(s) <= 1: # if string is empty or has only 1 char
        return s
    # take last char + middle part + first char
    return s[-1] + s[1:-1] + s[0]

s = input("Enter a string: ")
print("After swapping first and last character:",swap_first_last(s))

# DryRun
# "Python"
# s[-1] = 'n'
# s[1:-1] = 'ytho'
# s[0] = 'p


