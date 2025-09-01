import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print()
                print(f"Congratulations!\nCorrect Number: {number_to_guess} \nYou guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

guessing_game()
