import random

def game():
    print("Welcome to the Game!")
    score = random.randint(1, 50)
    with open("high_score.txt") as f:
        high_score = f.read()
        if high_score != "":
            high_score = int(high_score)
        else:
            high_score = 0
    print(f"Your score: {score}")
    if score > high_score:
        print("Congratulations! You have the new high score!")
        with open("high_score.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"The high score remains: {high_score}")

game()