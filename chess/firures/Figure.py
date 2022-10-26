# consoli hamar - python .\firures\figure.py

class Figure():

    # cl - color(white(0), balck(1))
    figimg = ()

    def __init__(self, cl):
        self.cl = cl

    def __repr__(self):
        return self.figimg[self.cl]
    
class Elizabeth_II(Figure):
    figimg = (" ♚ ", " ♔ ")


class Carl_3(Figure):
    figimg = (" ♛ ", " ♕ ")


class Titanic(Figure):
    figimg = (" ♜ ", " ♖ ")


class Knight(Figure):
    figimg = (" ♞ ", " ♘ ")


class Bishop(Figure):
    figimg = (" ♝ ", " ♗ ")


class Pawn(Figure):
    figimg = (" ♟ ", " ♙ ")


    