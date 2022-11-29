'''
Created on Mar 29, 2022
    This code is for the game 'rock, paper, scissors' it is between you and the computer.
    The game will ask you to pick either Rock, paper, or scissors. At the same time it will randomly choose the number a
     1, 2, or 3 each corresponding scissors, rock, and paper respectively. Once you and the computer have made your
     choice will announce the winner and points will be awarded. the game ends when someone reaches 3 points.
@author: athompson23
'''
import random
from termcolor import colored



def main():
    playerpoints = 0
    computerpoints = 0
    ok = True

    answer = input("Do you want to play a game?\n")
    if answer == 'yes':
        while answer == 'yes':
            player = input("rock, paper, or scissors?\n")
            computer = random.randint(1, 3)

            if player == 'scissors' and computer == 1:
                print(colored("you both played scissors so you tie",'white'))
                print(colored("you have " + str(playerpoints) + " points",'grey','on_white'))
                print(colored("computer has " + str(computerpoints) + " points",'grey','on_white'))

            elif player == 'rock' and computer == 2:
                print(colored("you both played rock so you tie",'grey'))
                print(colored("you have " + str(playerpoints) + " points", 'grey', 'on_white'))
                print(colored("computer has " + str(computerpoints) + " points", 'grey', 'on_white'))
            elif player == 'paper' and computer == 3:
                print(colored("you both played paper so you tie",'white'))
                print(colored("you have " + str(playerpoints) + " points", 'grey', 'on_white'))
                print(colored("computer has " + str(computerpoints) + " points", 'grey', 'on_white'))
            elif player == 'scissors' and computer == 3:
                print(colored("You won because the computer picked paper",'green'))
                playerpoints = playerpoints + 1
                computerpoints = computerpoints - 1
                print(colored("you have " + str(playerpoints) + " points", 'grey', 'on_white'))
                print(colored("computer has " + str(computerpoints) + " points", 'grey', 'on_white'))

            elif player == 'rock' and computer == 1:
                print(colored("You won because the computer picked scissors",'green'))
                playerpoints = playerpoints + 1
                computerpoints = computerpoints - 1
                print(colored("you have " + str(playerpoints) + " points", 'grey', 'on_white'))
                print(colored("computer has " + str(computerpoints) + " points", 'grey', 'on_white'))

            elif player == 'paper' and computer == 2:
                print(colored("You won because the computer picked rock",'green'))
                playerpoints = playerpoints + 1
                computerpoints = computerpoints - 1
                print(colored("you have " + str(playerpoints) + " points", 'grey', 'on_white'))
                print(colored("computer has " + str(computerpoints) + " points", 'grey', 'on_white'))

            elif player == 'scissors' and computer == 2:
                print(colored("You lost because the computer picked rock",'red'))
                playerpoints = playerpoints - 1
                computerpoints = computerpoints + 1
                print(colored("you have " + str(playerpoints) + " points", 'grey', 'on_white'))
                print(colored("computer has " + str(computerpoints) + " points", 'grey', 'on_white'))

            elif player == 'rock' and computer == 3:
                print(colored("You lost because the computer picked paper",'red'))
                playerpoints = playerpoints - 1
                computerpoints = computerpoints + 1
                print(colored("you have " + str(playerpoints) + " points", 'grey', 'on_white'))
                print(colored("computer has " + str(computerpoints) + " points", 'grey', 'on_white'))

            elif player == 'paper' and computer == 1:
                print(colored("You lost because the computer picked scissors",'red'))
                playerpoints = playerpoints - 1
                computerpoints = computerpoints + 1
                print(colored("you have " + str(playerpoints) + " points", 'grey', 'on_white'))
                print(colored("computer has " + str(computerpoints) + " points", 'grey', 'on_white'))

            if playerpoints == 3:
                print(colored(" Congrats your the big winner!",'green','on_grey'))

                while ok == True:
                    choice = input("Do you want to play again?\n")
                    if choice == 'yes':

                        ok = False
                        answer = 'yes'
                    elif choice == 'no':
                        ok = False
                        answer = 'no'
                    else:
                        print("please enter yes or no\n")
                        ok = True
            if computerpoints == 3:
                print(colored(" Sorry, but you have lost!",'red','on_grey'))

                while ok == True:
                    choice = input("Do you want to play again?\n")
                    if choice == 'yes':
                        ok = False
                        answer = 'yes'
                    elif choice == 'no':
                        ok = False
                        answer = 'no'
                    else:
                        print("please enter yes or no\n")
                        ok = True



    elif answer == "no":
        print("Goodbye")

    else:
        print("Please enter yes or no.")
        return main()


if __name__ == '__main__':
    main()

