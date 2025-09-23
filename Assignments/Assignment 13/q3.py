# Check if a Given key exists in a Dictionary

def key_exists(d, key):
    for k in d:
        if k == key:
            return True
    return False

dict = {"alpha":1, "beta":2}
print(key_exists(dict, "alpha")) # True
print(key_exists(dict, "z")) #False


