import random
import pyautogui as pg
from termcolor import colored


def turn_1(board, p1_hit):
    if spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
        return True
    if not spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
        return False


def turn_2(board, p2_hit):
    if spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
        return True
    if not spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
        return False


def spot_check(attack, spot_1, spot_2, spot_3, spot_4, spot_5):
    if spot_1 == attack or spot_2 == attack or spot_3 == attack or spot_4 == attack or spot_5 == attack:

        return True
    elif spot_1 != attack or spot_2 != attack or spot_3 != attack or spot_4 != attack or spot_5 != attack:

        return False


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


pg.alert("board position \n | 1 | 2 | 3 | 4 | 5 | \n | 6 | 7 | 8 | 9 |10 | \n |11 |12 |13 |14 |15 | \n |16 |17 |18 |19 "
         "|20 |\n |21 |22 |23 |24 |25 |\n player 1 is red, player 2 is blue")

board = " - - - - - \n - - - - - \n - - - - - \n - - - - - \n - - - - -"
p1_hit = 0
p2_hit = 0
x = 0
guess = 0
spot_1 = random.randint(1, 5)
spot_2 = random.randint(7, 11)
spot_3 = random.randint(13, 17)
spot_4 = random.randint(19, 23)
spot_5 = random.randint(25, 29)
while guess < 5:
    board = board.split(' ')
    attack = int(pg.prompt("P1, where do you want to play"))
    x = attack
    attack = position(x)
    if turn_1(board, p1_hit):
        pg.alert('hit')
        board[attack] = (colored("X", 'red'))
        board = (' '.join(map(str, board)))
        print(board)
        p1_hit = +1
    if not turn_1(board, p1_hit):
        pg.alert("miss")
        board[attack] = ("M")
        board = (' '.join(map(str, board)))
        print(board)
    print('---------------------------')
    board = board.split(' ')
    attack = int(pg.prompt("P2, where do you want to play"))
    x = attack
    attack = position(x)
    if turn_2(board, p2_hit):
        pg.alert('hit')
        board[attack] = (colored("X", 'blue'))
        board = (' '.join(map(str, board)))
        print(board)
        p2_hit = +1
    if not turn_2(board, p2_hit):
        pg.alert("miss")
        board[attack] = ("M")
        board = (' '.join(map(str, board)))
        print(board)
    print('---------------------------')
    guess += 1
else:
    if p1_hit > p2_hit:
        pg.alert('plqyer 1 wins')
        print('player 1 wins')
    elif p2_hit > p1_hit:
        pg.alert('player 2 wins')
        print('player 2 wins')
    elif p1_hit == p2_hit:
        pg.alert('Tie')
        print('Tie')
