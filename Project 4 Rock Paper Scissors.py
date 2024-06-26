rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 

user_choice = input("What do you choice? Type 0 for Rock, 1 for Paper, 2 for Scissors")

computer_choice = random.randint(0,2)
print(f"Computer choices: {computer_choice}")

if computer_choice == 0 and user_choice == 2:
    print("Computer Wins")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice > user_choice:
    print("Computer Wins")
elif user_choice > computer_choice:
    print("You Win")
elif computer_choice == user_choice:
    print("Its Draw")
else:
    print("Invalid Number, Enter a valid Number!")