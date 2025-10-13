# Union of two lists

def count_frequency(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

numbers = [1, 2, 4, 1, 2, 3, 6, 7, 1, 2, 4]
result = count_frequency(numbers)

print("Frequency of each number: ", result)