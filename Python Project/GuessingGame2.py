import random
print("Welcome to the Number Guessing Game!")
print("Pick The Difficulty Easy, Medium or hard")
diff = input("Difficulty  ")


def guessing_game():
    # Randomly select a number between 1 and 100
    secret_number = random.randint(1, 100)
    
   
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

#---------------------------------------------------------------------------------------------------------------
def guessing_game1():
    # Randomly select a number between 1 and 100
    secret_number = random.randint(1, 100)
  
    print("I'm thinking of a number between 1 and 100.")
    print("You have A Maximum Of 10 Attempts")


    
    maxAttempts = 10

    # Initialize the number of attempts
    attempts = 0
    
    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            maxAttempts -= 1
            
            # Check if the guess is correct, too high, or too low
            if guess < secret_number:
                print("You have " + str(maxAttempts) + " attempts left")
                print("Too low! Try again.")
                
            elif guess > secret_number:
                print("You have " + str(maxAttempts) + " attempts left")
                print("Too high! Try again.")
                
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop when the guess is correct

            if attempts == maxAttempts:
                print("You Have Reached The Maximum Attempts Allowed")
                print("The Secret Number is " + str(secret_number))
                break


        except ValueError:
            print("Please enter a valid number.")
#-------------------------------------------------------------------------------------------------------------

def guessing_game2():
    # Randomly select a number between 1 and 100
    secret_number = random.randint(1, 100)
    

    print("I'm thinking of a number between 1 and 100.")
    print("You have A Maximum Of 5 Attempts")


    
    maxAttempts = 5

    # Initialize the number of attempts
    attempts = 0
    
    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            maxAttempts -=1
            
            # Check if the guess is correct, too high, or too low
            if guess < secret_number:
                print("You have " + str(maxAttempts) + " attempts left")
                print("Too low! Try again.")
            elif guess > secret_number:
                print("You have " + str(maxAttempts) + " attempts left")
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop when the guess is correct

            if attempts == maxAttempts:
                print("You Have Reached The Maximum Attempts Allowed")
                print("The Secret Number is " + str(secret_number))
                break


        except ValueError:
            print("Please enter a valid number.")


if diff == "Easy":
    guessing_game()
elif diff == "Medium":
    guessing_game1()
elif diff == "Hard":
    guessing_game2()
elif diff == "easy":
    guessing_game()
elif diff == "medium":
    guessing_game1()
elif diff == "hard":
    guessing_game2()
elif diff == "EASY":
    guessing_game()
elif diff == "MEDIUM":
    guessing_game1()
elif diff == "HARD":
    guessing_game2()


    