import random

def guessing_game():
    # Randomly select a number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Initialize the number of attempts
    attempts = 0
    
    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct, too high, or too low
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop when the guess is correct
        except ValueError:
            print("Please enter a valid number.")

# Start the game
guessing_game()
