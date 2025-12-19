with open("poems.txt") as f:
    poems = f.readlines()
    for poem in poems:
        if "twinkle" in poem.lower():
            print("twinkle word is there in poem")