# Find the missing coin number

def missing_coin(coins):
    freq = {}
    
    for num in coins:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num, count in freq.items():
        if count % 2 != 0:
            return num
        
n = int(input("Enter total number of coins : "))
coins = list(map(int, input("Enter numbers on the remaining coins: ")))

missing = missing_coin(coins)
print("The missing coin number is:" , missing)
