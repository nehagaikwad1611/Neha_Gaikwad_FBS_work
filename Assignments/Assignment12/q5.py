# Count Number Of Vowels

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        for v in vowels:
            if ch == v:
                count += 1
    return count

s = input("Enter string: ")
print("Number Of Vowels in the String:",count_vowels(s))