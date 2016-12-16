import Othello
import pandas as pd
from os import listdir

class OthelloAI:
    def __init__(self, gamehost):
        if gamehost: self.gamehost = gamehost
        else: self.gamehost = Othello(True)
    
    def load_play_records(self):
        record_files = ['game_records/' + x for x in listdir('game_records')]
        for filepath in record_files:
            file = open(filepath)
            str = 'default'
            while str:
                pass
                
    
    def find_a_move(self, player, board):
        pass
    
    