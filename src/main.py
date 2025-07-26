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

def handle_edge_case(next_move):
    # Edges Cases: Null string, just x or y and just x or y but with space.
        if (len(next_move) < 2):
            print("Invalid position(s). Please try again!")
            return 1
        if (' ' not in next_move):
            print("Invalid separator. Please use space as separator")
            return 1

        x, y = next_move.split()
        
        # Edges about type: Float or char, ...
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print("Only integer allowed! Retry...")
            return 1
        if ((x < 0 or x > 8) or (y < 0 or y > 8)):
            print("Invalid position(s). Please try again!")
            return 1
        return x,y

def main():
    while True:
        next_move = input("Please enter your next move (x,y): ")
        print(next_move)
        
        if handle_edge_case(next_move) == 1:
            continue
        else:
            x, y = handle_edge_case(next_move)
            print(f"x:{x} y:{y}")
        
        draw_table()

if __name__ == "__main__":
    main()