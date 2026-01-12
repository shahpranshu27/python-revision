arr = [10, 2, 3, 4, 2, 10, 3, 6, 8, 10, 'a', 'b', 'a']
freq = {}

for char in arr:
    freq[char] = freq.get(char, 0) + 1

print(freq)