# Walrus operator assigns and returns value in one expression
# my_var is assigned "Hello World!" and then printed
print(my_var:="Hello World!")


# Data Types in Python

# Numbers
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# Text
name = "Alice"             # str

# Boolean
is_student = True          # bool

# None
result = None              # NoneType

# Collections
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set

# Concatenation and Replication

# String concatenation: adjacent strings are automatically joined
'Alice' 'Bob' # 'AliceBob'

# String replication: repeat string multiple times
'Alice' * 5 # 'AliceAliceAliceAliceAlice'

# Use sep parameter to specify separator between multiple arguments
print('cats', 'dogs', 'mice', sep=',')  # Comma-separated output