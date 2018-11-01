from random import randint

#available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

#make the computer pick one item at random
computer = choices[randint(0,2)]

#shows the computer choice in the terminal window
#(I commented the following line out because it ruins the point of the game! Hope that's okay!)
#print("Computer chooses: ", computer)

#3 lives for user and computer
userLives = 3
compLives = 3

while player == False:
    print("Choose Your Weapon")
    print("********************************")
    player = input("Rock, Paper or Scissors?\n")
    print("\nPlayer chooses:", player, "\n")

   #check for equality
    if (player == computer):
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
        #computer won
            print("You lose!", computer, "covers", player)
            #take away 1 life from user
            userLives = userLives - 1
        else:
            print("You win!", player, "smashes", computer)
            #take away 1 life from computer
            compLives = compLives - 1


    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            userLives = userLives - 1
        else:
            print("You win!", player, "covers", computer)
            compLives = compLives - 1

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            userLives = userLives - 1
        else:
            print("You win!", player, "cuts", computer)
            compLives = compLives - 1

    elif player == "Quit":
        exit()


    else:
        print("Not a valid option. Please verify your input and check your spelling\n")

    #show user players' lives
    print("\nYour Lives:", userLives)
    print("Compuer Lives:", compLives, "\n")

    #tell user (if) they lost
    if userLives == 0:
        print("This game is complete.\nThe Computer won, better luck next time!\n")
        print("********************************")
        playAgain = input("Would you like to play again? Type 'Yes' or 'No':\n")
        #ask user to play again
        if(playAgain == "Yes"):
            userLives = 3
            compLives = 3
        elif playAgain == "No":
            exit()
        else:
            print("Not a valid option. Please verify your input and check your spelling\n")

    #tell user (if) the computer lost
    elif compLives == 0:
        print("This game is complete.\nCongratulations, you won!\n")
        print("********************************")
        playAgain = input("Would you like to play again? Type 'Yes' or 'No':\n")
        if(playAgain == "Yes"):
            userLives = 3
            compLives = 3
        elif playAgain == "No":
            exit()
        else:
            print("Not a valid option. Please verify your input and check your spelling\n")

    player = False
    computer = choices[randint(0, 2)]
