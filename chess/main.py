import numpy as np
from firures import figure as fg

class Board():
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=fg.Figure)
        self.board.fill("•")

        # position of the black pieces

        self.board[0,0] = fg.Titanic(1)        
        self.board[0,7] = fg.Titanic(1)

        self.board[0,1] = fg.Knight(1)        
        self.board[0,6] = fg.Knight(1)  

        self.board[0,2] = fg.Bishop(1)        
        self.board[0,5] = fg.Bishop(1)  

        self.board[0,3] = fg.Carl_3(1)        
        self.board[0,4] = fg.Elizabeth_II(1)   

        for i in range(len(self.board[1])):
            self.board[1][i] = fg.Pawn(1)  


        # position of the white pieces

        self.board[7,0] = fg.Titanic(0)        
        self.board[7,7] = fg.Titanic(0)

        self.board[7,1] = fg.Knight(0)        
        self.board[7,6] = fg.Knight(0)  

        self.board[7,2] = fg.Bishop(0)        
        self.board[7,5] = fg.Bishop(0)  

        self.board[7,3] = fg.Carl_3(0)        
        self.board[7,4] = fg.Elizabeth_II(0)   

        for i in range(len(self.board[0])):
            self.board[6][i] = fg.Pawn(0)             



print(Board().board)