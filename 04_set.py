# Sets

s = {1,2,3}
print(s)

empty_set = set()  # Correct way to create an empty set, and not {} as this will create an empty dictionary

set1 = {1, 1.0, '1', [2,3]} # This will raise a TypeError because lists are unhashable and cannot be added to a set
print(set1)