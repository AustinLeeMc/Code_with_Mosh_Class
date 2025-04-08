# Loop
# Generate a random number 1 - 100
# Ask the user to guess the number
# tell the user if the guess is too high or low
# allow the user to guess until the number is chosen
#
#
#

import random
number = []
number_to_guess = random.randint(1, 101)
lives = 6

while True:
    number = number_to_guess
    choice = int(input("Guess the number between 1 and 100"))
    if choice > number:
        print("Too high!")
        lives -= 1
    elif choice < number:
        print("Too low!")
        lives -= 1
    elif choice == number:
        print("Congratulations you guessed the number!")
        break
    else:
        print("Invalid choice")
        lives -= 1
    if lives == 0:
        print(f"The number was {number_to_guess}!")
        print("Out of guesses, Game Over!")
        break