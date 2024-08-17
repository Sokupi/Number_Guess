import random

print("\n Welcome to the Number Game!")  # Header
print()


def random_number_generator():
    while True:
        secret_number = random.randint(1, 100)  # Generates a random number between 1 and 100
        attempts = 0  # This variable records the attempts the user makes

        while True:
            # Puts in the input of the user
            guess = input(f"Attempts made {attempts}, Guess a number between 1 and 100: ")

            if not guess.isdigit():  # Checks the input for it to be integers
                print("Please enter a number")
                continue

            guess = int(guess)  # Turns the string type number into integer type

            if guess < 1 or guess > 100:  # Make sure the input to be 1 and 100
                print("Please enter a number between 1 and 100")
                continue

            attempts += 1  # Adds 1 value after user's input

            if guess < secret_number:  # Tells the user if the input is too low
                print("Too low, try again")

            elif guess > secret_number:  # Tells the user if the input is too high
                print("Too high, try again")

            else:
                print(f"You guessed it in {attempts} tries")  # Tells how many attempts after the user is done
                break

        play_again = input("Do you want to play again? (yes/no): ").lower()  # Retry the game
        if play_again != 'yes':
            print("Thanks for playing!")
            break


random_number_generator()