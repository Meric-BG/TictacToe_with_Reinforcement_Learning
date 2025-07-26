import numpy as np

"""OOP in Python. My first Python class here: TicTacToe. With all about the game: The table and his dimensions
    Players, game state"""

# Feel free to change the table dimensions and the player symbols. 
class TicTacToe():
    def __init__(self):
        self.nb_rows = 3
        self.nb_cols = 3
        self.table = [[' ' for _ in range(self.nb_cols)] for _ in range(self.nb_rows)] 
        self.p1_symbol = 'O' 
        self.p2_symbol = 'X'
        self.Game_over = False

def draw_table(Game):
    for i in range(Game.nb_rows):
        for j in range(Game.nb_cols):
            print(f"|{Game.table[i][j]}", end='')
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
        if ((x < 0 or x > 2) or (y < 0 or y > 2)):
            print("Invalid position(s). Please try again!")
            return 1
        return x,y

def victory_checkor(Game):
    s1 = 0
    s2 = 0

    # Rows checking
    for i in range(Game.nb_rows):
        for j in range(Game.nb_cols):
            if Game.table[i][j] == Game.p1_symbol:
               s1 =+ 1
            if Game.table[i][j] == Game.p2_symbol:
               s2 =+ 1
        if s1 == 3:
            print("Player 1 won!")
            return 1
        if s2 == 3:
            print("Player 2 won!")
            return 2
        s1 = s2 = 0
    
    # Cols checking
    for j in range(Game.nb_cols):
        for i in range(Game.nb_rows):
            if Game.table[i][j] == Game.p1_symbol:
               s1 =+ 1
            if Game.table[i][j] == Game.p2_symbol:
               s2 =+ 1
        if s1 == 3:
            print("Player 1 won!")
            return 1
        if s2 == 3:
            print("Player 2 won!")
            return 2
        s1 = s2 = 0

    # Diagonals checking
    for i in range(Game.nb_rows):
        #--Upper Left to Down Right's logic------Down Left to Upper Right's logic-------
        if Game.table[i][i] == Game.p1_symbol or Game.table[2 - i][i] == Game.p1_symbol:
           s1 =+ 1
        if Game.table[i][i] == Game.p2_symbol or Game.table[2 - i][i] == Game.p2_symbol:
           s2 =+ 1
    if s1 == 3:
        print("Player 1 won!")
        return 1
    if s2 == 3:
        print("Player 2 won!")
        return 2


def main():
    Game = TicTacToe()
    counter = 0
    while True:
        next_move = input("Please enter your next move (x,y): ")
        print(next_move)
        
        #Edges cases
        if handle_edge_case(next_move) == 1:
            continue
        else:
            x, y = handle_edge_case(next_move)
            # Filling the game with  the right symbol
            print(f"cou:{counter}")
            Game.table[x][y] = Game.p1_symbol if counter % 2 == 0 else Game.p2_symbol
            draw_table(Game)
            victory_checkor(Game)
        counter =+ 1

if __name__ == "__main__":
    main()