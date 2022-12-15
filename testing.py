import random
import pyautogui as pg
from termcolor import colored
from playsound import playsound
# change random spots to inputs from players, need a board_2, pg.alert the board, add stop time to allow for
# switching computer, Figure out how to make ships bigger
# make a def ship_spot


def spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
    if spot_1 == attack or spot_2 == attack or spot_3 == attack or spot_4 == attack or spot_5 == attack:

        return True
    elif spot_1 != attack or spot_2 != attack or spot_3 != attack or spot_4 != attack or spot_5 != attack:

        return False

    if spot_6 == attack or spot_7 == attack or spot_8 == attack or spot_9 == attack or spot_10 == attack:

        return True
    elif spot_6 != attack or spot_7 != attack or spot_8 != attack or spot_9 != attack or spot_10 != attack:

        return False


def spot_check2(attack):
    if board[attack] == '💦' or board[attack] == '🔥':
        return False
    elif board[attack] == '⚈':
        return True
    elif board2[attack] == '💦' or board2[attack] == '🔥':
        return False
    elif board2[attack] == '⚈':
        return True


def position(x):  # takes the position given by the player and tells code which spot in the list to change
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    elif x == 4:
        return 4
    elif x == 5:
        return 5
    elif x == 6:
        return 7
    elif x == 7:
        return 8
    elif x == 8:
        return 9
    elif x == 9:
        return 10
    elif x == 10:
        return 11
    elif x == 11:
        return 13
    elif x == 12:
        return 14
    elif x == 13:
        return 15
    elif x == 14:
        return 16
    elif x == 15:
        return 17
    elif x == 16:
        return 19
    elif x == 17:
        return 20
    elif x == 18:
        return 21
    elif x == 19:
        return 22
    elif x == 20:
        return 23
    elif x == 21:
        return 25
    elif x == 22:
        return 26
    elif x == 23:
        return 27
    elif x == 24:
        return 28
    elif x == 25:
        return 29


def ship_spot1(spot_1, spot_2, spot_3, spot_4, spot_5):
    spot_1 = int(pg.prompt('player 1 give 1st ship position'))
    spot_2 = int(pg.prompt('player 1 give 2nd ship position'))
    spot_3 = int(pg.prompt('player 1 give 3rd ship position'))
    spot_4 = int(pg.prompt('player 1 give 4th ship position'))
    spot_5 = int(pg.prompt('player 1 give 5th ship position'))


def ship_spot2(spot_6, spot_7, spot_8, spot_9, spot_10):
    spot_6 = int(pg.prompt('player 2 give 1st ship position'))
    spot_7 = int(pg.prompt('player 2 give 2nd ship position'))
    spot_8 = int(pg.prompt('player 2 give 3rd ship position'))
    spot_9 = int(pg.prompt('player 2 give 4th ship position'))
    spot_10 = int(pg.prompt('player 2 give 5th ship position'))


pg.alert("board position \n | 1 | 2 | 3 | 4 | 5 | \n | 6 | 7 | 8 | 9 |10 | \n |11 |12 |13 |14 |15 | \n |16 |17 |18 |19 "
         "|20 |\n |21 |22 |23 |24 |25 |\n player 1 is red, player 2 is blue, each player will pick the position of 5 ships each one "
         "is one dot big, both players have 10 guesses to find the other players ships. Wwho ever has hit the most ships "
         "at the end of 10 guesses wins")
p1_hit = 0
p2_hit = 0
x = 0
guess = 0
pg.alert("PLEASE ENTER NUMBERS ONLY")
spot_1 = int(pg.prompt('player 1 give 1st ship position'))
if spot_1 > 25:
    spot_1 = pg.prompt("invalid number entered, please give a number 1-25")
spot_2 = int(pg.prompt('player 1 give 2nd ship position'))
if spot_2 > 25:
    spot_2 = pg.prompt("invalid number entered, please give a number 1-25")
spot_3 = int(pg.prompt('player 1 give 3rd ship position'))
if spot_3 > 25:
    spot_3 = pg.prompt("invalid number entered, please give a number 1-25")
spot_4 = int(pg.prompt('player 1 give 4th ship position'))
if spot_4 > 25:
    spot_4 = pg.prompt("invalid number entered, please give a number 1-25")
spot_5 = int(pg.prompt('player 1 give 5th ship position'))
if spot_5 > 25:
    spot_5 = pg.prompt("invalid number entered, please give a number 1-25")

if spot_1 == spot_2 and spot_3 and spot_3 and spot_4 and spot_5:
    pg.alert("Yo you put a ship in the same spot, now you have to pick ship spots again")
    if spot_1 > 25:
        spot_1 = pg.prompt("invalid number entered, please give a number 1-25")
    spot_2 = int(pg.prompt('player 1 give 2nd ship position'))
    if spot_2 > 25:
        spot_2 = pg.prompt("invalid number entered, please give a number 1-25")
    spot_3 = int(pg.prompt('player 1 give 3rd ship position'))
    if spot_3 > 25:
        spot_3 = pg.prompt("invalid number entered, please give a number 1-25")
    spot_4 = int(pg.prompt('player 1 give 4th ship position'))
    if spot_4 > 25:
        spot_4 = pg.prompt("invalid number entered, please give a number 1-25")
    spot_5 = int(pg.prompt('player 1 give 5th ship position'))
    if spot_5 > 25:
        spot_5 = pg.prompt("invalid number entered, please give a number 1-25")

pg.alert('please give computer to player 2')


spot_6 = int(pg.prompt('player 2 give 1st ship position'))
if spot_6 > 25:
    spot_6 = pg.prompt("invalid number entered, please give a number 1-25")
spot_7 = int(pg.prompt('player 2 give 2nd ship position'))
if spot_7 > 25:
    spot_7 = pg.prompt("invalid number entered, please give a number 1-25")
spot_8 = int(pg.prompt('player 2 give 3rd ship position'))
if spot_8 > 25:
    spot_8 = pg.prompt("invalid number entered, please give a number 1-25")
spot_9 = int(pg.prompt('player 2 give 4th ship position'))
if spot_9 > 25:
    spot_9 = pg.prompt("invalid number entered, please give a number 1-25")
spot_10 = int(pg.prompt('player 2 give 5th ship position'))
if spot_10 > 25:
    spot_10 = pg.prompt("invalid number entered, please give a number 1-25")
if spot_6 == spot_7 and spot_8 and spot_9 and spot_10:
    if spot_6 > 25:
        spot_6 = pg.prompt("invalid number entered, please give a number 1-25")
    spot_7 = int(pg.prompt('player 2 give 2nd ship position'))
    if spot_7 > 25:
        spot_7 = pg.prompt("invalid number entered, please give a number 1-25")
    spot_8 = int(pg.prompt('player 2 give 3rd ship position'))
    if spot_8 > 25:
        spot_8 = pg.prompt("invalid number entered, please give a number 1-25")
    spot_9 = int(pg.prompt('player 2 give 4th ship position'))
    if spot_9 > 25:
        spot_9 = pg.prompt("invalid number entered, please give a number 1-25")
    spot_10 = int(pg.prompt('player 2 give 5th ship position'))
    if spot_10 > 25:
        spot_10 = pg.prompt("invalid number entered, please give a number 1-25")






pg.alert('please give computer to player 1')
board = " ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈"
board2 = " ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈ \n ⚈ ⚈ ⚈ ⚈ ⚈"
while guess < 10:

    attack = int(pg.prompt("P1, where do you want to play"))
    board2 = board2.split(' ')
    x = attack
    attack = position(x)
    if not spot_check2(attack):
        print('you can not play there')
        attack = int(pg.prompt("new position"))
        spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5)
    if spot_check2(attack):
        if spot_check(attack, spot_6, spot_7, spot_8, spot_9, spot_10):
            pg.alert('hit') and playsound(r"C:\Users\athompson23\Desktop\ggg.mp3")
            board2[attack] = (colored("🔥", 'red'))
            board2 = (' '.join(map(str, board2)))
            p1_hit += 1
            print(board2)

        if not spot_check(attack, spot_6, spot_7, spot_8, spot_9, spot_10):
            pg.alert("miss") and playsound(r"C:\Users\athompson23\Desktop\www.mp3")
            board2[attack] = (colored("💦", 'red'))
            board2 = (' '.join(map(str, board2)))
            print(board2)
    print('---------------------------')
    pg.alert('please give computer to player 2')
#-------------------------------------------------------------------------------------------
    attack = int(pg.prompt("P2, where do you want to play"))
    board = board.split(' ')
    x = attack
    attack = position(x)
    if not spot_check2(attack):
        print('you can not play there')
        attack = int(pg.prompt("new position"))
        spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5)
    if spot_check2(attack):
        if spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
            pg.alert('hit') and playsound(r"C:\Users\athompson23\Desktop\ggg.mp3")
            board[attack] = (colored("🔥", 'blue'))
            board = (' '.join(map(str, board)))
            p2_hit += 1
            print(board)
        if not spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
            pg.alert("miss") and playsound(r"C:\Users\athompson23\Desktop\www.mp3")
            board[attack] = (colored("💦", 'blue'))
            board = (' '.join(map(str, board)))
            print(board)
    print('---------------------------')
    guess += 1
else:
    if p1_hit > p2_hit:
        score = str(p1_hit - p2_hit)
        pg.alert('player 1 won by ' + score + ' points')
        print('player 1 wins')
    elif p2_hit > p1_hit:
        score = str(p2_hit - p1_hit)
        pg.alert('player 2 won by ' + score + ' points')
        print('player 2 wins')
    elif p1_hit == p2_hit:
        pg.alert('Tie')
        print('Tie')


