import random

target = random.randint(1, 10)

attempts = 3

print("Welcome! Guess the number between 1 and 10.")

print(f"You have {attempts} attempts.")

while attempts > 0:

    try:

        guess = int(input(f"\nRemaining attempts: {attempts}. Enter your guess: "))


        if guess == target:

            print("Congratulations! You guessed it right!")

            break # Exit the loop if the guess is correct

        elif guess < target:

            print("Too low!")

        else:

            print("Too high!")


        attempts = attempts - 1


    except ValueError:

        print("Invalid input. Please enter a whole number.")

if attempts == 0:

    print(f"\nGame Over! The correct number was {target}.")