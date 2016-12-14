"""
test-board
"""
tboard = [
['.','.','.','.','.','.','.','.'],
['.','.','1','0','0','.','.','.'],
['.','.','0','1','1','.','.','.'],
['.','1','1','0','1','.','.','.'],
['.','.','.','1','0','.','.','.'],
['.','.','0','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
]

iboard = [
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
]

import pandas as pd

class Othello(object):
    def __init__(self, istest):
        self.black_piece = '0'
        self.white_piece = '1'
        self.empty_cell = '.'
        self.board_width = 8
        self.board_height = 8
        
        if istest:
            self.board = pd.DataFrame(tboard)
        else:
            self.board = pd.DataFrame(iboard)
            self.board[self.board_width / 2 - 1][self.board_height / 2 - 1] = self.black_piece
            self.board[self.board_width / 2][self.board_height / 2] = self.black_piece
            self.board[self.board_width / 2 - 1][self.board_height / 2] = self.white_piece
            self.board[self.board_width / 2][self.board_height / 2 - 1] = self.white_piece
        
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
            while tx <= self.board_width - 1:
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
            while ty < self.board_height - 1:
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
            while tx >= 0 and ty <= self.board_height - 1:
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
            while tx <= self.board_width - 1 and ty >= 0:
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
            while tx <= self.board_width - 1 and ty <= self.board_height - 1:
                if self.board[tx][ty] == self.empty_cell:break
                if self.board[tx][ty] == player:
                    destination.append((tx, ty))
                    break
                tx += 1
                ty += 1   
                
        return destination
    
    def reverse_cell(self, player, x, y, tx, ty):
        iincrement = (tx - x) / abs(tx - x) if tx != x else 0
        jincrement = (ty - y) / abs(ty - y) if ty != y else 0
        i = x + iincrement
        j = y + jincrement
        while i != tx or j != ty:
            self.board[i][j] = player
            i = i + iincrement
            j = j + jincrement
    
    def get_possible_moves(self, player):
        for x in xrange(self.board_width):
            for y in xrange(self.board_height):
                result = self.get_reversion_solution(player, x, y)
                if len(result) > 0:
                    yield (x, y)
    
    def make_a_move(self, player, x, y):
        result = self.get_reversion_solution(player, x, y)
        if (x, y) in self.get_possible_moves(player):
            self.board[x][y] = player
            for tx, ty in result:
                self.reverse_cell(player, x, y, tx, ty)
        
o = Othello(True)
o.board
o.reverse_cell('1',5,4,3,4)
o.board