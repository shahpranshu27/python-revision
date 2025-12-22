word = ["Donkey", "Monkey", "Turkey"]

with open("donkey.txt") as f:
    content = f.read()
    print(content)

for w in word:
    content = content.replace(w, len(w)*"#")

with open("donkey.txt", "w") as f:
    f.write(content)
    print(content)