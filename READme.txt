Hello! This is now my 5th project which is a game called "Number Guess".
This will generate a number which the user would then need to guess, each guess would then be told of how closer they are on the answer.
If you're looking to create one on you're own as well, here are my steps:

Objective 1: Import Required Modules

- Import the random module, which will help you generate a random number.

Objective 2: Generate a Random Number

- Use the random.randint() function to generate a number between 1 and 100. This will be the secret number the user has to guess.

Objective 3: Get User Input

- Ask the user to guess the number.
- Ensure that the input is a valid number (you can use .isdigit() to check this).

Objective 4: Check the User's Guess

- Compare the user’s guess to the secret number:
    If the guess is too high, print a message like "Too high! Try again."
    If the guess is too low, print a message like "Too low! Try again."
    If the guess is correct, congratulate the user.

Objective 5: Count the Number of Attempts

- Keep track of how many guesses the user makes.
- When the user guesses the correct number, display how many attempts they took.

Objective 6: Loop Until the Correct Guess

- Continue to ask the user for a guess until they guess the correct number.

Bonus Objective (Optional): Add Input Validation

- If the user enters something that isn't a number, prompt them to enter a valid number.

Once you complete these objectives, your "Number Guess" game will be ready!