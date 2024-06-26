#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Tip Calculator!")

bill = float(input("What is your total bill?\n"))

people = int(input("Between how many people are you going to split the bill?\n"))

tip = int(input("How much is the tip?\n"))

tips = (tip/100)*bill

total = (bill+tips)/people

amount =round(total, 2)

print("Each person should pay: {0}".format(amount))