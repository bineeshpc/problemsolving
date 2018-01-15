""" Backtracking problem 8 queens"""
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

class Enum(object):
    empty = 0
    queen = 1
    
class ChessBoard(object):
    def __init__(self, size):
        self.size = size
        self.board = [[Enum.empty for i in range(self.size)]
                      for j in range(self.size)]
        self.queen_location = []

    def place_queen(self, x, y):
        """ When we place a queen all the rows and columns must
be marked as already attacked. Increment the number by one"""
        # increment the rows values after placing queen
        for i in range(self.size):
            self.board[x][i] += 1

        # increment the columns values after placing queen
        for i in range(self.size):
            self.board[i][y] += 1

        # increment the diagonal values after placing queen
        # ladder on left wall
        i = x
        j = y
        while i >= 0 and j >= 0:
            self.board[i][j] += 1
            i -= 1
            j -= 1

        i = x
        j = y
        while i < self.size and j < self.size:
            self.board[i][j] += 1
            i += 1
            j += 1



        # increment the diagonal values after placing queen
        # ladder on right wall
        i = x
        j = y
        while i < self.size and j >= 0:
            self.board[i][j] += 1
            i += 1
            j -= 1


        i = x
        j = y
        while i >= 0 and j < self.size:
            self.board[i][j] += 1
            i -= 1
            j += 1



    
    def remove_queen(self, x, y):
        """ When we place a queen all the rows and columns must
be marked as already attacked. Increment the number by one"""
        # increment the rows values after placing queen
        for i in range(self.size):
            self.board[x][i] -= 1

        # increment the columns values after placing queen
        for i in range(self.size):
            self.board[i][y] -= 1

        # increment the diagonal values after placing queen
        # ladder on left wall
        i = x
        j = y
        while i >= 0 and j >= 0:
            self.board[i][j] -= 1
            i -= 1
            j -= 1

        i = x
        j = y
        while i < self.size and j < self.size:
            self.board[i][j] -= 1
            i += 1
            j += 1



        # increment the diagonal values after placing queen
        # ladder on right wall
        i = x
        j = y
        while i < self.size and j >= 0:
            self.board[i][j] -= 1
            i += 1
            j -= 1


        i = x
        j = y
        while i >= 0 and j < self.size:
            self.board[i][j] -= 1
            i -= 1
            j += 1


    def is_attacked(self, x, y):
        return self.board[x][y] > 0

    def find_conf(self, x, y):
        """ starting from 0,0 try to place queen
Place it in first vacant place.
If I cannot proceed and backtrack"""
        if not self.is_attacked(x, y):
            self.queen_location.append((x, y))
            logging.debug("placed at {}, {}".format(x, y))
            logging.debug(self.queen_location)
            self.place_queen(x, y)
            logging.debug(cb)
            if x == (self.size - 1):
                return
            else:
                self.find_conf(x+1, 0)
        else:  # not attacked
            if y+1 < self.size:
                self.find_conf(x, y+1)
            else:
                x1, y1 = self.queen_location.pop()
                self.remove_queen(x1, y1)
                logging.debug("removed from".format(x1, y1))
                logging.debug(self.queen_location)
                logging.debug(cb)
                if y1 + 1 < self.size:
                    self.find_conf(x1, y1+1)
                else:
                    if self.queen_location != []:
                        x1, y1 = self.queen_location.pop()
                        self.remove_queen(x1, y1)
                        logging.debug("removed from".format(x1, y1))
                        logging.debug(self.queen_location)
                        logging.debug(cb)
                        if y1 + 1 < self.size:
                            self.find_conf(x1, y1+1)
        
    def __str__(self):
        return '\n' + '\n'.join([str(self.board[i]) for i in range(self.size)])

    def queen_location_print(self):
        print
        a = []
        
        for i in range(self.size):
            a.append([])
            x, y = self.queen_location[i]
            for j in range(self.size):
                if i == x and j == y:
                    a[i].append('Q')
                else:
                    a[i].append('_')

        
        for i in range(self.size):
            print a[i]
        

cb = ChessBoard(8)

cb.find_conf(0, 0)

print cb
print cb.queen_location

print cb.queen_location_print()
