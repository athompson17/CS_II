import random
import pyautogui as pg
from termcolor import colored
from playsound import playsound


# change random spots to inputs from players, need a board_2, pg.alert the board, add stop time to allow for
# make a def ship_spot
def position(letter, number):  # takes the position given by the player and converts it to number corresponding with
    # a board position
    if letter == 'a' and number == 1 or letter == 'A' and number == 1:
        return 1
    elif letter == 'b' and number == 1 or letter == 'B' and number == 1:
        return 2
    elif letter == 'c' and number == 1 or letter == 'C' and number == 1:
        return 3
    elif letter == 'd' and number == 1 or letter == 'D' and number == 1:
        return 4
    elif letter == 'e' and number == 1 or letter == 'E' and number == 1:
        return 5
    elif letter == 'a' and number == 2 or letter == 'A' and number == 2:
        return 7
    elif letter == 'b' and number == 2 or letter == 'B' and number == 2:
        return 8
    elif letter == 'c' and number == 2 or letter == 'C' and number == 2:
        return 9
    elif letter == 'd' and number == 2 or letter == 'D' and number == 2:
        return 10
    elif letter == 'e' and number == 2 or letter == 'E' and number == 2:
        return 11
    elif letter == 'a' and number == 3 or letter == 'A' and number == 3:
        return 13
    elif letter == 'b' and number == 3 or letter == 'B' and number == 3:
        return 14
    elif letter == 'c' and number == 3 or letter == 'C' and number == 3:
        return 15
    elif letter == 'd' and number == 3 or letter == 'D' and number == 3:
        return 16
    elif letter == 'e' and number == 3 or letter == 'E' and number == 3:
        return 17
    elif letter == 'a' and number == 4 or letter == 'A' and number == 4:
        return 19
    elif letter == 'b' and number == 4 or letter == 'B' and number == 4:
        return 20
    elif letter == 'c' and number == 4 or letter == 'C' and number == 4:
        return 21
    elif letter == 'd' and number == 4 or letter == 'D' and number == 4:
        return 22
    elif letter == 'e' and number == 4 or letter == 'E' and number == 4:
        return 23
    elif letter == 'a' and number == 5 or letter == 'A' and number == 5:
        return 25
    elif letter == 'b' and number == 5 or letter == 'B' and number == 5:
        return 26
    elif letter == 'c' and number == 5 or letter == 'C' and number == 5:
        return 27
    elif letter == 'd' and number == 5 or letter == 'D' and number == 5:
        return 28
    elif letter == 'e' and number == 5 or letter == 'E' and number == 5:
        return 29


def spot_check(attack, board, board2):  # checks if either player has guessed a spot yet
    if board[attack] == (colored("💦", 'blue')) or board[attack] == (colored("🔥", 'blue')):
        pg.alert('you can not play there')
        attack = (pg.prompt("new position"))
        letter = str(attack[0:1])
        number = int(attack[1:])
        attack = position(number, letter)
        spot_check(attack, board, board2)
    elif board2[attack] == (colored("💦", 'red')) or board2[attack] == (colored("🔥", 'red')):
        pg.alert('you can not play there')
        attack = (pg.prompt("new position"))
        letter = str(attack[0:1])
        number = int(attack[1:])
        attack = position(number, letter)
        spot_check(attack, board, board2)
    elif board2[attack] == '⚈':
        return
    elif board[attack] == '⚈':
        return


def spot_check2(attack, spot_1, spot_2, spot_3, spot_4, spot_5):  # function that checks if payer 1's guess was a hit
    if spot_1 == attack or spot_2 == attack or spot_3 == attack or spot_4 == attack or spot_5 == attack:

        return True
    elif spot_1 != attack or spot_2 != attack or spot_3 != attack or spot_4 != attack or spot_5 != attack:

        return False


def spot_check3(attack, spot_6, spot_7, spot_8, spot_9, spot_10):  # function that checks if payer 2's guess was a hit
    if spot_6 == attack or spot_7 == attack or spot_8 == attack or spot_9 == attack or spot_10 == attack:

        return True
    elif spot_6 != attack or spot_7 != attack or spot_8 != attack or spot_9 != attack or spot_10 != attack:

        return False


def boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10):
    if spot_1 == spot_2:  # sends to function that checks if that location has already been entered
        spot_2 = pg.prompt('you have already put a ship there\n Please enter a new position')
        letter = str(spot_2[0:1])
        number = int(spot_2[1:])
        spot_2 = position(letter, number)
        boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)
    elif spot_3 == spot_2 or spot_3 == spot_1:
        spot_3 = pg.prompt('you have already put a ship there\n Please enter a new position')
        letter = str(spot_3[0:1])
        number = int(spot_3[1:])
        spot_3 = position(letter, number)
        boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)
    elif spot_4 == spot_3 or spot_4 == spot_2 or spot_4 == spot_1:
        spot_4 = pg.prompt('you have already put a ship there\n Please enter a new position')
        letter = str(spot_4[0:1])
        number = int(spot_4[1:])
        spot_4 = position(letter, number)
        boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)
    elif spot_5 == spot_3 or spot_5 == spot_4 or spot_5 == spot_2 or spot_5 == spot_1:
        spot_5 = pg.prompt('you have already put a ship there\n Please enter a new position')
        letter = str(spot_5[0:1])
        number = int(spot_5[1:])
        spot_5 = position(letter, number)
        boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)
    elif spot_7 == spot_6:
        spot_7 = pg.prompt('you have already put a ship there\n Please enter a new position')
        letter = str(spot_7[0:1])
        number = int(spot_7[1:])
        spot_7 = position(letter, number)
        boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)
    elif spot_8 == spot_6 or spot_8 == spot_7:
        spot_8 = pg.prompt('you have already put a ship there\n Please enter a new position')
        letter = str(spot_8[0:1])
        number = int(spot_8[1:])
        spot_8 = position(letter, number)
        boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)
    elif spot_9 == spot_6 or spot_9 == spot_7 or spot_9 == spot_8:
        spot_9 = pg.prompt('you have already put a ship there\n Please enter a new position')
        letter = str(spot_9[0:1])
        number = int(spot_9[1:])
        spot_9 = position(letter, number)
        boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)
    elif spot_10 == spot_6 or spot_10 == spot_7 or spot_10 == spot_8 or spot_10 == spot_9:
        spot_10 = pg.prompt('you have already put a ship there\n Please enter a new position')
        letter = str(spot_10[0:1])
        number = int(spot_10[1:])
        spot_10 = position(letter, number)
        boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)



# introduction to the game, with some rules
pg.alert("board position\n    a  b  c  d  e\n 1 ⚈ ⚈ ⚈ ⚈ ⚈ \n 2 ⚈ ⚈ ⚈ ⚈ ⚈ \n 3 ⚈ ⚈ ⚈ ⚈ ⚈ \n 4 ⚈ ⚈ ⚈ ⚈ ⚈ \n 5 ⚈ ⚈ ⚈ ⚈ ⚈ "
         "\nplayer 1 is red, player 2 is blue, each player will pick the position of 5 ships each one "
         "is one dot big, both players have 10 guesses to find the other players ships. Who ever has hit the most "
         "ships "
         "at the end of the 10 guesses wins \nexample inputs: A1, b4, C5, d2, E3 ")
p1_hit = 0
#  these keep track of each player's number of hits
p2_hit = 0
guess = 0
#   ____________________
spot_1 = 0
spot_2 = 200
spot_3 = 300
spot_4 = 400
spot_5 = 500
spot_6 = 600
spot_7 = 700
spot_8 = 800
spot_9 = 900
spot_10 = 100
#   ____________________
# ______________________________________________________________________
# asks for both players positions
spot_1 = str(pg.prompt('player 1 give 1st ship position'))

letter = str(spot_1[0:1])
number = int(spot_1[1:])
spot_1 = position(letter, number)

spot_2 = str(pg.prompt('player 1 give 2nd ship position'))
letter = str(spot_2[0:1])
number = int(spot_2[1:])
spot_2 = position(letter, number)
boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)

spot_3 = str(pg.prompt('player 1 give 3rd ship position'))
letter = str(spot_3[0:1])
number = int(spot_3[1:])
spot_3 = position(letter, number)
boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)

spot_4 = str(pg.prompt('player 1 give 4th ship position'))
letter = str(spot_4[0:1])
number = int(spot_4[1:])
spot_4 = position(letter, number)
boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)

spot_5 = str(pg.prompt('player 1 give 5th ship position'))
letter = str(spot_5[0:1])
number = int(spot_5[1:])
spot_5 = position(letter, number)
boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)

pg.alert('please give the computer to player 2')

spot_6 = str(pg.prompt('player 2 give 1st ship position'))
letter = str(spot_6[0:1])
number = int(spot_6[1:])
spot_6 = position(letter, number)

spot_7 = str(pg.prompt('player 2 give 2nd ship position'))
letter = str(spot_7[0:1])
number = int(spot_7[1:])
spot_7 = position(letter, number)
boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)

spot_8 = str(pg.prompt('player 2 give 3rd ship position'))
letter = str(spot_8[0:1])
number = int(spot_8[1:])
spot_8 = position(letter, number)
boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)

spot_9 = str(pg.prompt('player 2 give 4th ship position'))
letter = str(spot_9[0:1])
number = int(spot_9[1:])
spot_9 = position(letter, number)
boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)



spot_10 = str(pg.prompt('player 2 give 5th ship position'))
letter = str(spot_10[0:1])
number = int(spot_10[1:])
spot_10 = position(letter, number)
boat_positions(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10)

board = " ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈"  # player 1's guess board
board2 = " ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈"  # player 2's guess board
while guess < 3:
    pg.alert('please give computer to player 1')  # pause given to allow for th players to switch the computer around
    attack = str(
        pg.prompt("\n    a  b  c  d  e\n 1 ⚈ ⚈ ⚈ ⚈ ⚈ \n 2 ⚈ ⚈ ⚈ ⚈ ⚈ \n 3 ⚈ ⚈ ⚈ ⚈ ⚈ \n 4 ⚈ ⚈ ⚈ ⚈ ⚈ \n 5 ⚈ ⚈ ⚈ ⚈ ⚈"
                  "\nP1, where do you want to play"))  # prompt to ask player 1 for their attack position
    board2 = board2.split(' ')  # turns board from string to list
    letter = str(attack[0:1])  # takes first character of the input
    number = int(attack[1:])  # takes second character of the input and turns it into an int
    attack = position(letter, number)  # converts the input into a number which translates to a position on the board

    spot_check(attack, board, board2)
    if spot_check3(attack, spot_6, spot_7, spot_8, spot_9, spot_10):  # checks if the guess is a hit
        pg.alert('hit') and playsound(r"C:\Users\athompson23\Desktop\ggg.mp3")  # plays explosion sound
        board2[attack] = (colored("🔥", 'red'))  # puts hit sign in the proper location
        board2 = (' '.join(map(str, board2)))  # turns board back into a list
        p1_hit += 1
        print(board2)

    if not spot_check3(attack, spot_6, spot_7, spot_8, spot_9, spot_10):  # checks if the guess was a miss
        pg.alert("miss") and playsound(r"C:\Users\athompson23\Desktop\www.mp3")  # plays water drop sound
        board2[attack] = (colored("💦", 'red'))  # prints miss icon where ever the player missed
        board2 = (' '.join(map(str, board2)))  # turns board into string
        print(board2)
    print('---------------------------')
    pg.alert('please give computer to player 2')
    # -------------------------------------------------------------------------------------------
    # (all the same just for player 2)
    attack = str(
        pg.prompt("\n    a  b  c  d  e\n 1 ⚈ ⚈ ⚈ ⚈ ⚈ \n 2 ⚈ ⚈ ⚈ ⚈ ⚈ \n 3 ⚈ ⚈ ⚈ ⚈ ⚈ \n 4 ⚈ ⚈ ⚈ ⚈ ⚈ \n 5 ⚈ ⚈ ⚈ ⚈ ⚈"
                  "\nP2, where do you want to play"))
    board = board.split(' ')
    letter = str(attack[0:1])
    number = int(attack[1:])
    attack = position(letter, number)

    spot_check(attack, board, board2)
    if spot_check2(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
        pg.alert('hit') and playsound(r"C:\Users\athompson23\Desktop\ggg.mp3")
        board[attack] = (colored("🔥", 'blue'))
        board = (' '.join(map(str, board)))
        p2_hit += 1
        print(board)
    if not spot_check2(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
        pg.alert("miss") and playsound(r"C:\Users\athompson23\Desktop\www.mp3")
        board[attack] = (colored("💦", 'blue'))
        board = (' '.join(map(str, board)))
        print(board)
    print('---------------------------')
    guess += 1
else:  # checks which player has won
    if p1_hit > p2_hit:  # player 1 wins
        score = str(p1_hit - p2_hit)
        pg.alert('player 1 won by ' + score + ' points')
        print('player 1 wins')
    elif p2_hit > p1_hit:  # player 2 wins
        score = str(p2_hit - p1_hit)
        pg.alert('player 2 won by ' + score + ' points')
        print('player 2 wins')
    elif p1_hit == p2_hit:  # there is a tie
        pg.alert('Tie')
        print('Tie')
