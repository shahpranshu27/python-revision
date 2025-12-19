f = open("file.txt")
content = f.read()
print(content)
f.close()

st = "This is a sample text file"
f = open("myfile.txt", "w")
f.write(st)
f.close()

# readlines()
f = open("file.txt")
data = f.readlines()
print(data)
f.close()

# readline()
f = open("file.txt")
l1 = f.readline()
print("l1: ", l1)
l2 = f.readline()
print("l2: ", l2)
l3 = f.readline()
print("l3: ", l3)
l4 = f.readline()
print("l4: ", l4)
l5 = f.readline()
print("l5: ", l5) # will print empty string as EOF reached
f.close()

# readline() in loop
f = open("file.txt")
line = f.readline()
while line != "":
    print("line: ", line)
    line = f.readline()
f.close()

# append mode
f = open("file.txt", "a")
f.write("\nThis is appended line")
f.close()


# The same using 'with' statement
with open("file.txt") as f:
    print(f.read())

# No need to write f.close(), it is done automatically