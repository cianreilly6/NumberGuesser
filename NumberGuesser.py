import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Define the range of numbers
    low = 1
    high = 100
    print(f"I'm thinking of a number between {low} and {high}.")

    # Generate a random number
    number_to_guess = random.randint(low, high)

    # Initialize the number of guesses
    guess_count = 0
    guessed_correctly = False

    # Game loop
    while not guessed_correctly:
        guess_count += 1
        try:
            # Ask the user to make a guess
            guess = int(input(f"Attempt {guess_count}: Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {guess_count} attempts.")
            break

# Run the game
number_guessing_game()
