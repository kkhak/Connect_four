#
# ps11pr4.py (Problem Set 11, Problem 4)
#
# An AI Player for use in Connect Four
#
import random
from ps10pr3 import * # to use the connect_four and process_move functions
from ps10pr1 import Board

class AIPlayer(Player):
    """intelligent connect 4 player subclass that inherits from player class"""
    
    def __init__(self, checker, tiebreak, lookahead):
        """Constructs an AIPlayer object."""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """Return a string representation of the AIPlayer."""
        return f"Player {self.checker} ({self.tiebreak}, {self.lookahead})"
    
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column 
        of the board, and that returns the index of the column with 
        the maximum score."""
        max_score = max(scores)
        max_indices = [i for i, score in enumerate(scores) if score == max_score]
        
        if self.tiebreak == 'LEFT':
            return max_indices[0]
        elif self.tiebreak == 'RIGHT':
            return max_indices[-1]
        else:
            return random.choice(max_indices)
    
    def scores_for(self, board):
        """Determine the scores for each column in the board."""
        scores = [50] * board.width
        
        for col in range(board.width):
            if not board.can_add_to(col):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                
                if board.is_win_for(self.checker):
                    scores[col] = 100
                else:
                    opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                    opp_scores = opponent.scores_for(board)
                    
                    if max(opp_scores) == 0:
                        scores[col] = 100
                    elif max(opp_scores) == 100:
                        scores[col] = 0
                    else:
                        scores[col] = 50
                
                board.remove_checker(col)
        
        return scores
    
    def next_move(self, board):
        """Determine the next move for the AIPlayer."""
        scores = self.scores_for(board)
        best_col = self.max_score_column(scores)
        self.num_moves += 1
        return best_col
