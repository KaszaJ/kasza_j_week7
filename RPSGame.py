from random import randint

#available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

#make the computer pick one item at random
computer = choices[randint(0,2)]

#3 lives for user and computer
userLives = 3
compLives = 3


#define a win or lose function instead of procedural way
def winOrLose(status):
    #handle win or lose based on the status we pass in
    print("Called the win or lose function")
    print("********************************")
    print("You", status, "!", "Would you like to play again?")
    choice = input("Y / N: ")

    if choice == "Y" or choice == "y":
        #reset the game
        #change global variables
        global compLives
        global userLives
        global player
        global computer

        compLives = 3
        userLives = 3
        player = False
        computer = choices[randint(0,2)]

    elif choice == "N" or choice == "n":
        print("You chose to quit.")
        exit()


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
        winOrLose("lost")

    #tell user (if) the computer lost
    elif compLives == 0:
        winOrLose("won")

    player = False
    computer = choices[randint(0, 2)]
