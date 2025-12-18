# Dictionary
marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Alice": 23 # Duplicate key, will overwrite previous value for "Alice"
}

print(marks)

print(marks.get("Alice")) # Output: 85
print(marks["Alice"]) # Output: 85

print(marks.get("Alice2")) # Output: None
# print(marks["Alice2"]) # KeyError: 'Alice2'

print(marks.items())