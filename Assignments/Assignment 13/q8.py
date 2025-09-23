# Count Frequency of Words in a string using dictionary

def word_frequency(s):
    words = s.split(" ")
    freq = {}
    for w in words:
        count = 0
        for i in words:
            if w == i:
                count += 1
        freq[w] = count
    return freq
s = "apple mango apple orange mango apple"
print("Word Frequency:" ,word_frequency(s))