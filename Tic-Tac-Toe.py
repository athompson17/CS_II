"""
Created on November 11, 2022,
Description: The game of Tic-Tac-Toe
@author: athompson23
Bugs: none
"""


def player(new_board, x):  # checks if there is an X or O where someone is trying to play
    if new_board[position(x)] == '-':  # if there is no X or O it allows you to play
        return True
    elif new_board[position(x)] != '-':  # if there is an X or O, and then it has you replay
        return False and new_board


def turn_p1(new_board):  # ask where player 1 would like to play, it also checks if someone has played in that spot yet
    x = int(input('player 1, give position'))  # asks for position

    if player(new_board, x):  # if the space is open you can play there
        new_board[position(x)] = 'x'  # change the desired position to X
        new_board = (' '.join(map(str, new_board)))  # turns the list into a string
        return new_board
    elif not player(new_board, x):
        print("you can not play there, go again")
        x = int(input('give new position'))

        if player(new_board, x):  # if the desired spot is taken it will ask for a new position
            new_board[position(x)] = 'x'
            new_board = (' '.join(map(str, new_board)))
            return new_board
        else:
            print('you do not get another chance, game over')


def turn_p2(new_board):  # ask where player 2 would like to play, it also checks if someone has played in that spot yet
    x = int(input('player 2, give position'))  # asks for position

    if player(new_board, x):  # if the space is open you can play there
        new_board[position(x)] = 'o'  # change the desired position to O
        new_board = (' '.join(map(str, new_board)))  # turns the list into a string
        return new_board
    elif not player(new_board, x):  # if the desired spot is taken it will ask for a new position
        print('you can not play there, go again')
        x = int(input('give new position'))
        if player(new_board, x):
            new_board[position(x)] = 'o'
            new_board = (' '.join(map(str, new_board)))
            return new_board
        else:
            print('you do not get another chance, game over')


def position(x):  # takes the position given by the player and tells code which spot in the list to change
    if x == 1:
        return 2
    elif x == 2:
        return 3
    elif x == 3:
        return 4
    elif x == 4:
        return 6
    elif x == 5:
        return 7
    elif x == 6:
        return 8
    elif x == 7:
        return 10
    elif x == 8:
        return 11
    elif x == 9:
        return 12  #


def check_win(new_board):  # function that checks to see if either player has won
    new_board = new_board.split(' ')
    if new_board[2] == 'x' and new_board[3] == 'x' and new_board[4] == 'x':  # conditionals if X wins
        end = True
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 1 wins')
        return end
    elif new_board[6] == 'x' and new_board[7] == 'x' and new_board[8] == 'x':  # conditionals if X wins

        (' '.join(map(str, new_board)))
        end = True
        print('game over, player 1 wins')
        return end
    elif new_board[10] == "x" and new_board[11] == "x" and new_board[12] == 'x':  # conditionals if X wins

        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 1 wins')
        end = True
        return end
    elif new_board[2] == "x" and new_board[6] == "x" and new_board[10] == 'x':  # conditionals if X wins
        print('game over, player 1 wins')
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        end = True
        print('game over, player 1 wins')
        return end
    elif new_board[3] == "x" and new_board[7] == "x" and new_board[11] == 'x':  # conditionals if X wins

        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        end = True
        print('game over, player 1 wins')
        return end
    elif new_board[4] == "x" and new_board[8] == "x" and new_board[12] == 'x':  # conditionals if X wins

        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        end = True
        print('game over, player 1 wins')
        return end
    elif new_board[2] == "x" and new_board[7] == "x" and new_board[12] == 'x':  # conditionals if X wins

        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 1 wins')
        end = True
        return end
    elif new_board[4] == "x" and new_board[7] == "x" and new_board[10] == 'x':  # conditionals if X wins

        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        end = True
        print('game over, player 1 wins')
        return end
    elif new_board[2] == "o" and new_board[3] == "o" and new_board[4] == 'o':  # conditionals if O wins

        end = True
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 2 wins')
        return end
    elif new_board[6] == "o" and new_board[7] == "o" and new_board[8] == 'o':  # conditionals if O wins
        print('game over, player 2 wins')
        end = True
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 2 wins')
        return end
    elif new_board[10] == "o" and new_board[11] == "o" and new_board[12] == 'o':  # conditionals if O wins
        print('game over, player 2 wins')
        end = True
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 2 wins')
        return end
    elif new_board[2] == "o" and new_board[6] == "o" and new_board[10] == 'o':  # conditionals if O wins
        print('game over, player 2 wins')
        end = True
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 2 wins')
        return end
    elif new_board[3] == "o" and new_board[7] == "o" and new_board[11] == 'o':  # conditionals if O wins

        end = True
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 2 wins')
        return end
    elif new_board[4] == "o" and new_board[8] == "o" and new_board[12] == 'o':  # conditionals if O wins

        end = True
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 2 wins')
        return end
    elif new_board[2] == "o" and new_board[7] == "o" and new_board[12] == 'o':  # conditionals if O wins

        end = True
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 2 wins')
        return end
    elif new_board[4] == "o" and new_board[7] == "o" and new_board[10] == 'o':  # conditionals if O wins

        end = True
        new_board = (' '.join(map(str, new_board)))
        print(new_board)
        print('game over, player 2 wins')
        return end
    else:  # if no one wins then continue playing
        end = False
        return end


def main():
    try:
        print("board position \n | 1 | 2 | 3 | \n | 4 | 5 | 6 | \n | 7 | 8 | 9 |")  # prints board positions
        game = 0  # loop starts

        new_board = " \n - - - \n - - - \n - - -"  # original board
        while game < 4:  # while loop that counts how many moves have been made
            new_board = new_board.split(' ')  # turns board into a list instead of a string

            new_board = turn_p1(new_board)  # calls function that asks for player 1's position, returns new_board with
            # their move
            print(new_board)  # prints new_board with the move
            if check_win(new_board):  # calls the function that checks if someone has won
                wait = input('press enter to restart')
                if wait == '':
                    return main()
                else:
                    break  #
            new_board = new_board.split(' ')  # turns string of new_board into a list

            new_board = turn_p2(new_board)  # calls function that asks for player 1's position, returns new_board with
            # their move
            print(new_board)  # prints new_board with the move
            if check_win(new_board):  # calls the function that checks if someone has won
                wait = input('press enter to restart')
                if wait == '':
                    return main()
                else:
                    break

            game += 1  # adds 1 to game to continue loop
        else:  # after player 1 and 2 have both played 4 times and no one has won player 1 still has a final turn
            # this asks for their turn and then asks if the players wish to restart
            player_1 = input('player 1, give position')
            new_board = player(player_1, new_board)
            new_board = (' '.join(map(str, new_board)))
            print(new_board)
            wait = input('press enter to restart')  # asks if players wish to restart
            if wait == '':
                return main()

    except ValueError:
        print("you did not enter data correctly, restarting")
        return main()


if __name__ == '__main__':
    main()
