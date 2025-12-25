from functools import reduce

# Map example

l = [1, 2, 3, 4, 5]
square = lambda x: x*x

# map(function, iterable)
sqlList = map(square, l)
print("Map Result:", list(sqlList))

# Filter example
# filter(function, iterable)
even = lambda x: x%2 == 0
evenList = filter(even, l)
print("Filter Result:", list(evenList))

# Reduce example
# reduce(function, iterable)
sumFunc = lambda x, y: x + y
print("Reduce Result:", reduce(sumFunc, l))

def greater(a, b):
    return a if a > b else b
print("Max using Reduce:", reduce(greater, l))