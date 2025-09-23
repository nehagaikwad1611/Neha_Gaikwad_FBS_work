#Concat 2 dictionaries into one

def concat_dict(d1, d2):
        d3 = {} 
        # copy d1        # loop through keys of d2
        for k in d1:
            d3[k] = d1[k]
        # Copy d2
        for k in d2:
            d3[k] = d2[k]
        return d3

d1 = {1:"A", 2:"B"}
d2 = {3:"C", 4:"D"}
print("Concatenated Dictionary:",concat_dict(d1, d2))