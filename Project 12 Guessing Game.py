#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo

number = randint(1,100)

def easy(number):
    attempt = 10
    while attempt>0:
        print(f"You have {attempt} attempts remaining to guess a number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.\n Guess again.")
        elif guess < number:
            print("Too low.\n Guess again.")
        elif guess == number:
            print(f"You won! The answer was {number}")
            break
        attempt -= 1
    
    if attempt == 0:
        print("You lost!\n Try Again")

def hard(number):
    attempt = 5
    while attempt>0:
        print(f"You have {attempt} attempts remaining to guess a number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.\n Guess again.")
        elif guess < number:
            print("Too low.\n Guess again.")
        elif guess == number:
            print(f"You won! The answer was {number}")
            break

        attempt -= 1
    
    if attempt == 0:
        print("You lost!\n Try Again")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
choice = input("Choose Difficulty. Type 'easy' or 'hard':")

if choice == 'easy':
    easy(number)
else:
    hard(number)