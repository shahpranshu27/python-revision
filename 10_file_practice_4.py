word = "Donkey"

with open("donkey.txt") as f:
    content = f.read()
    print(content)
    
contentNew = content.replace(word, "####")
with open("donkey.txt", "w") as f:
    f.write(contentNew)
    print(contentNew)