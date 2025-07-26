import numpy as np

"""OOP in Python. My first Python class here: TicTacToe. With all about the game: The table and his dimensions
    Players, game state"""

class TicTacToe():
    def __init__(self, p1, p2):
        self.nb_rows = 3
        self.nb_cols = 3
        self.table = [[' ' for _ in range(self.nb_cols)] for _ in range(self.nb_rows)] 
        self.p1 = p1
        self.p2 = p2
        self.Game_over = False

def draw_table():
    nb_rows = 3
    nb_cols = 3
 
    table = [[' ' for _ in range(nb_cols)] for _ in range(nb_rows)] 
   
    for i in range(nb_rows):
        for j in range(nb_cols):
            print(f"|{table[i][j]}", end='')
            # C must also have thing like that
            print('|', end='') if j == 2 else ""
        print('')

if __name__ == "__main__":
    draw_table()