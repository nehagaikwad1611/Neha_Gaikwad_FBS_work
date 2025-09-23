# Count Number Of Words and Characters

def count_words_char(s):
    char_count = 0
    if s:
        word_count = 1  # if string is not empty
    else:
        word_count = 0  # If string is empty

    for ch in s:
        char_count += 1
        if ch == " ":
            word_count += 1
    return word_count, char_count

s = input("Enter a string: ")
words, chars = count_words_char(s)
print("Words:", words)
print("Characters:", chars)
