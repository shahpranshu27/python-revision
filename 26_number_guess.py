from random import randint

def guess_number():
    number_to_guess = randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    while True:
        user_input = input("Please enter your guess (between 1 and 100): ")
        attempts += 1
        
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess < 1 or guess > 100:
            print("Your guess is out of bounds. Please guess a number between 1 and 100.")
            continue
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
        
guess_number()