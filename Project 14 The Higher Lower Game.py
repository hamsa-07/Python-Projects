
from game_data import data
import random
from art import logo1,logo2
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(choice):
    choice_name = choice["name"]
    choice_desc = choice["description"]
    choice_country = choice["country"]
    return f"Compare A: {choice_name}, {choice_desc}, {choice_country}."

def check_answer(guess, a_fol, b_fol):
    if a_fol > b_fol:
        return guess == "A"
    else:
        return guess == "B"

score = 0
game = True
choice_a = get_random_account()
choice_b = get_random_account()
while game:
    choice_a = choice_b
    choice_b = random.choice(data)

    while choice_a == choice_b:
        choice_b = random.choice(data)

    print(logo1)
    print(f"Compare A: {format_data(choice_a)}")
    print(logo2)
    print(f"Compare B: {format_data(choice_b)}")

    guess = input("Who has more followers? Type A or B: ").upper()
    a_fol = choice_a["follower_count"]
    b_fol = choice_b["follower_count"]

    is_crt = check_answer(guess, a_fol, b_fol)

    clear()

    if is_crt:
        score += 1
        print(f"You are right! your score {score}")
    else:
        print(f"You are wrong! your score {score}")

