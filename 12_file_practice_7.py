

with open("log.txt") as f:
    lines = f.readlines()

line_no = 1
for line in lines:
    if ("python" in line):
        print("Python is present: ", line_no)
        break
    line_no += 1
else:
    print("Python is not present")