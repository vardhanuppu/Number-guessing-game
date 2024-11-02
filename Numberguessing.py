
import random

def guess_the_number():
    lower_bound = 1
    upper_bound = 100
    max_attempts = 10
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Welcome to 'Guess the Number'! I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it correctly.")
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if guess < number_to_guess:
                print(f"Too low! You have {remaining_attempts} attempts remaining.")
            elif guess > number_to_guess:
                print(f"Too high! You have {remaining_attempts} attempts remaining.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid integer.")
    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}. Better luck next time!")
guess_the_number()
