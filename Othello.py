"""
test-board
"""
tboard = [
['1','.','.','.','.','.','.','.'],
['1','0','.','.','.','.','.','.'],
['1','0','.','.','0','.','.','.'],
['1','1','1','1','1','1','.','.'],
['1','1','1','1','0','0','.','.'],
['1','0','1','1','1','0','0','0'],
['1','1','1','1','1','.','.','.'],
['1','1','1','0','.','.','.','.'],
]

t1board = [
['1','1','1','1','0','1','1','1'],
['1','0','1','1','1','0','1','0'],
['1','0','1','0','0','0','1','0'],
['1','1','1','1','1','1','1','0'],
['1','1','1','1','0','0','1','.'],
['1','0','1','1','1','0','0','0'],
['1','1','1','1','1','0','1','1'],
['1','1','1','0','1','1','1','1'],
]

iboard = [
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','1','0','.','.','.'],
['.','.','.','0','1','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
]

import pandas as pd
import datetime

class Othello(object):
    def __init__(self, istest):
        
        self.black_piece = '0'
        self.white_piece = '1'
        self.empty_cell = '.'
        self.board_width = 8
        self.board_height = 8
        self.isstarted = False    
        self.istest = istest
        
        if self.istest:
            self.board = pd.DataFrame(t1board)
        else:
            self.board = pd.DataFrame(iboard)
    
    def get_reversion_solution(self, player, x, y):
        destination = []
        if self.board[x][y] != self.empty_cell: 
            return destination
        """
        leftwards
        """
        if x > 0 and self.board[x - 1][y] != self.empty_cell and self.board[x - 1][y] != player:
            tx = x - 1
            while tx >= 0:
                if self.board[tx][y] == self.empty_cell:break
                if self.board[tx][y] == player:
                    destination.append((tx, y))
                    break
                tx -= 1
        
        """
        rightwards
        """
        if x < self.board_width - 1 and self.board[x + 1][y] != self.empty_cell and self.board[x + 1][y] != player:
            tx = x + 1
            while tx < self.board_width:
                if self.board[tx][y] == self.empty_cell:break
                if self.board[tx][y] == player:
                    destination.append((tx, y))
                    break
                tx += 1
        """
        upwards
        """
        if y > 0 and self.board[x][y - 1] != self.empty_cell and self.board[x][y - 1] != player:
            ty = y - 1
            while ty >= 0:
                if self.board[x][ty] == self.empty_cell:break
                if self.board[x][ty] == player:
                    destination.append((x, ty))
                    break
                ty -= 1
        
        """
        downwards
        """
        if y < self.board_height - 1 and self.board[x][y + 1] != self.empty_cell and self.board[x][y + 1] != player:
            ty = y + 1
            while ty < self.board_height:
                if self.board[x][ty] == self.empty_cell:break
                if self.board[x][ty] == player:
                    destination.append((x, ty))
                    break
                ty += 1
        
        """
        left-up wards
        """
        if x > 0 and y > 0 and self.board[x - 1][y - 1] != self.empty_cell and self.board[x - 1][y - 1] != player:
            tx = x - 1
            ty = y - 1
            while tx >= 0 and ty >= 0:
                if self.board[tx][ty] == self.empty_cell:break
                if self.board[tx][ty] == player:
                    destination.append((tx, ty))
                    break
                tx -= 1
                ty -= 1
        
        """
        left-down wards
        """
        if x > 0 and y < self.board_height - 1 and self.board[x - 1][y + 1] != self.empty_cell and self.board[x - 1][y + 1] != player:
            tx = x - 1
            ty = y + 1
            while tx >= 0 and ty < self.board_height:
                if self.board[tx][ty] == self.empty_cell:break
                if self.board[tx][ty] == player:
                    destination.append((tx, ty))
                    break
                tx -= 1
                ty += 1  
        
        """
        right-up wards
        """
        if x < self.board_width - 1 and y > 0 and self.board[x + 1][y - 1] != self.empty_cell and self.board[x + 1][y - 1] != player:
            tx = x + 1
            ty = y - 1
            while tx < self.board_width and ty >= 0:
                if self.board[tx][ty] == self.empty_cell:break
                if self.board[tx][ty] == player:
                    destination.append((tx, ty))
                    break
                tx += 1
                ty -= 1
                
        """
        right-down wards
        """
        if x < self.board_width - 1 and y < self.board_height - 1 and self.board[x + 1][y + 1] != self.empty_cell and self.board[x + 1][y + 1] != player:
            tx = x + 1
            ty = y + 1
            while tx < self.board_width and ty < self.board_height:
                if self.board[tx][ty] == self.empty_cell:break
                if self.board[tx][ty] == player:
                    destination.append((tx, ty))
                    break
                tx += 1
                ty += 1   
                
        return destination
    
    def reverse_cell(self, piece, x, y, tx, ty):
        iincrement = (tx - x) / abs(tx - x) if tx != x else 0
        jincrement = (ty - y) / abs(ty - y) if ty != y else 0
        i = x + iincrement
        j = y + jincrement
        while i != tx or j != ty:
            self.board[i][j] = piece
            i = i + iincrement
            j = j + jincrement
    
    def get_possible_moves(self, piece):
        for x in xrange(self.board_width):
            for y in xrange(self.board_height):
                result = self.get_reversion_solution(piece, x, y)
                if len(result) > 0:
                    yield (x, y)
                    
    def check_game_status(self):
        black_moves = self.get_possible_moves(self.black_piece)
        white_moves = self.get_possible_moves(self.white_piece)
        total_black_pieces = sum(self.board[self.board == self.black_piece].count())
        total_white_pieces = sum(self.board[self.board == self.white_piece].count())
        return (black_moves != 0 or white_moves != 0) and total_black_pieces != 0 and total_white_pieces != 0 and (total_black_pieces + total_white_pieces) != self.board_width * self.board_height
    
    def make_a_move(self, piece, x, y):
        if not self.isstarted: return False
        result = self.get_reversion_solution(piece, x, y)
        if len(result):
            self.board[x][y] = piece
            """
            log move
            """
            if not self.istest: 
                for i in xrange(self.board_width):
                    for j in xrange(self.board_height):
                        self.log.write(self.board[i][j])
                    self.log.write('\n')
                self.log.write("{0},{1}\n".format(x, y))
                
            for tx, ty in result:
                self.reverse_cell(piece, x, y, tx, ty)
        if not self.check_game_status():
            self.end_game()
        return True
            
    def start_game(self):
        self.isstarted = True
        self.board = pd.DataFrame(iboard)
        """
        Create log file for game records
        """
        if not self.istest:
            time = datetime.datetime.now()
            logfilename = 'game_records/{0}-{1}-{2}-{3}{4}{5}.txt'.format(time.year, time.month, time.day, time.hour, time.minute, time.second)
            self.log = open(logfilename, 'w+')
            self.log.write(str(time) + '\n')
            print "log file : {0}".format(logfilename)
            
        print "Game is started."
        
    def end_game(self):
        self.isstarted = False
        total_black_piece = sum(self.board[self.board==self.black_piece].count())
        total_white_piece = sum(self.board[self.board==self.white_piece].count())
        if total_black_piece > total_white_piece : 
            print 'Game over. Black wins.'
            if not self.istest: self.log.write("Finished,B\n")
        if total_black_piece == total_white_piece : 
            print 'Game over. Fair.'
            if not self.istest: self.log.write("Unfinished,N\n")
        if total_black_piece < total_white_piece : 
            print 'Game over. White wins.'
            if not self.istest:  self.log.write("Finished,W\n")
        if not self.istest:
            self.log.flush()
            self.log.close()
        
class OperationError(Exception):
    pass
        
#o = Othello(False)
#o.board