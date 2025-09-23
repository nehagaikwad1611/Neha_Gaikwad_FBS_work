# Add a key-Value pair to the dictionary

def add_pair(d, key, value):
    d[key] = value  # If we write dictionary[new_key]= value it adds new key- value pair # Direct assignment
    return d

d = {1:"Apple", 2:"Brazil", 3:"Germany"}
key = 4
value = "Japan"
print("Updated Dictionary:" ,add_pair(d, key, value))
