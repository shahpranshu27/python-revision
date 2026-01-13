def remove_duplicate(name):
    name1 = []
    for char in name:
        if char not in name1:       
            name1.append(char)
    
    return ''.join(name1)

print(remove_duplicate("hello world"))