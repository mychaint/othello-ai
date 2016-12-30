import Othello
import pandas as pd
from os import listdir
from os.path import isfile, join

class OthelloAI:
    def __init__(self, gamehost):
        if gamehost: self.gamehost = gamehost
        else: self.gamehost = Othello(True)
    
    def load_play_records(self):
        record_names = [f for f in listdir('game_records') if isfile(join('game_records', f))]
        for filename in record_names:
            record = open(filename)
            string = record.readline()
            n = 1
            dataset = {}
            data = []
            while string:
                string = record.readline()
                data.append([x for x in string])
                if i % 8 == 0:
                    dataset[]
                            
    def find_a_move(self, player, board):
        pass
    
    