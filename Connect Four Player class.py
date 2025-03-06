#kyle hakimi, kylehaki@bu.edu
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#

from ps10pr1 import Board

# Write your class below.

class Player:
    """represent a player of the Connect Four game"""
    #constructor
    def __init__(self, checker):
        assert checker in ['X', 'O'], "Checker must be either 'X' or 'O'"
        self.checker = checker
        self.num_moves = 0
        #repr method
    def __repr__(self):
        return f"Player {self.checker}"
#method 3
    def opponent_checker(self):
        """returns a one-character string representing the checker
        of the Player object’s opponent."""
        if self.checker == 'X' :
            return 'O' 
        else: 
            return 'X'
#method 4
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns the 
        column where the player wants to make the next move. """
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col):
                self.num_moves += 1
                return col
            else:
                print('Try again!')
