#kyle Hakimi, kylehaki@bu.edu
# ps10pr3.py (Problem Set 10, Problem 3)
#
# Playing the game
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board

def process_move(p, b):
    """takes two parameters: a Player object p for the player 
    whose move is being processed, and a Board object b for the 
    board on which the game is being played. The function will
    perform all of the steps involved in processing a single 
    move by player p on board b."""
   
    print(f"{p}'s turn")
    
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    
    print()
    print(b)
    
    if b.is_win_for(p.checker):
        print(f"{p} wins in {p.num_moves} moves.")
        print("Congratulations!")
        return True
    if b.is_full():
        print("It's a tie!")
        return True
    else:
        return False

#client code to start game 
player1 = Player('X')
player2 = Player('O')
game_board = connect_four(player1, player2)