from random import randint

# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]

# make the computer pick one item at random
computer_choice = choices[randint(0,2)]

# show the computer's choice in the terminal window
print("Computer chooses: ", computer_choice)