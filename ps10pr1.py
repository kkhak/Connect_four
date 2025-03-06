#Kyle Hakimi, kylehaki@bu.edu
# ps10pr1.py (Problem Set 10, Problem 1)
#
# Problem 1: A Connect Four Board class
#
# Computer Science 111
#


class Board:
    """ data type for a connect four board with arbitrary dimesions"""
    def __init__(self, height, width):
        """ a constructor for Board objects"""
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
     #repr method   
    def __repr__(self):
        """ Returns a string representation for a Board object."""
        s = ''    # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

    # Add code here for the hyphens at the bottom of the board
    # and the numbers underneath it.
        s += '-' * (self.width * 2 + 1) + '\n'
        
        #colum numbers
        s += ' '
        
        for col in range(self.width):
            s += str(col % 10) + ' '
    
        return s
    #method 3
    def add_checker(self, checker, col):
        """
        Add a checker to the board in the specified column.
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # Find the first empty row in the specified column
        for row in range(self.height - 1, -1, -1):
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                break
    
    #method 4
    def reset(self):
        """ reset the Board object on which it is called by 
        setting all slots to contain a space character."""
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
    
    #method 5
    
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
    #method 6
        
    def can_add_to(self, col):
        """returns True if it is valid to place a checker in the 
        column col on the calling Board object. Otherwise, it 
        should return False."""
        if col < 0 or col >= self.width:
            return False
        return self.slots[0][col] == ' '
    
    #method 7
    def is_full(self):
        """returns True if the called Board object is completely full of 
        checkers, and returns False otherwise."""
        for col in range(self.width):
            if self.can_add_to(col):
                return False
            else:
                return True
    #method 8
    
    def remove_checker(self, col):
        """removes the top checker from column col of the 
        called Board object."""
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break 
            
    # method 9
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False

    def is_vertical_win(self, checker):
        """checks for vertical win"""
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """cheks down diagonal win"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """cheks up diagonal win"""
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False
   
    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or 
        'O', and returns True if there are four consecutive 
        slots containing checker on the board. Otherwise, 
        it should return False."""
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker):
            return True
        if self.is_vertical_win(checker):
            return True
        if self.is_down_diagonal_win(checker):
            return True
        if self.is_up_diagonal_win(checker):
            return True
        
        return False
