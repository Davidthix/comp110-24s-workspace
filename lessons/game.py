"""Number guessing game."""
from random import randint

SECRET: int = randint(1,5)
correct: bool = False

while not correct: # correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    elif guess < SECRET:
        print(f"{guess} is too low!")
    else:
        print(f"{guess} is too high!")
