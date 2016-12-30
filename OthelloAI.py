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
        dataset = []
        for file_name in record_names:
            data = load_data_from_file(file_name)
            dataset.extend(data)
        pass
    
    def load_data_from_file(file_name):
        file = open(file_name)
        

    def find_a_move(self, player, board):
        pass
    
    