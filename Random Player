#kyle hakimi, kylehaki@bu.edu
# ps11pr3.py (Problem Set 11, Problem 3)
#
# An RandomPlayer for use in Connect Four
#

import random
from ps10pr3 import * # to use the connect_four and process_move functions

import random
from ps10pr2 import Player
from ps10pr1 import Board

class RandomPlayer(Player):
    """untintelligent player class that inherits from player and create subclass"""
    def next_move(self, board):
        """ Chooses at random from the available columns in the board """
        available_cols = [col for col in range(board.width) if board.can_add_to(col)]
        chosen_col = random.choice(available_cols)
        self.num_moves += 1
        return chosen_col

