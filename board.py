
from const import *
from square import Square
from piece import *

class Board:
    
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(cols)] #Creation des cases de l'équiquier
        self._create()
        self._add_piece("white") #on place les pieces blanches
        self._add_piece("black") #on place les pieces noires

    def _create(self):
        '''
        Instancie un objet square à chaque case de l'échiquier
        '''
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col]=Square(row,col)

    def _add_piece(self,color):
        '''
        Ajoute les pieces d'un des joueurs (color) sur l'echiquier à leur case de départ pour débuter la partie
        '''
        (row_pawns,row_others) = (6,7) if color=="white" else (1,0)

        #Pawns
        for col in range(cols):
            self.squares [row_pawns][col] = Square(row_pawns,col, Pawn(color))

        #Knights
        self.squares [row_others][1] = Square(row_pawns,1, Knight(color))
        self.squares [row_others][6] = Square(row_pawns,6, Knight(color))

        #Bishops
        self.squares [row_others][2] = Square(row_pawns,2, Bishop(color))
        self.squares [row_others][5] = Square(row_pawns,5, Bishop(color))

        #Rooks
        self.squares [row_others][0] = Square(row_pawns,0, Rook(color))
        self.squares [row_others][7] = Square(row_pawns,7, Rook(color))

        #Queen
        self.squares [row_others][3] = Square(row_pawns,5, Queen(color))

        #King
        self.squares [row_others][4] = Square(row_pawns,4, King(color))

    def new_piece_position(self, piece, old_position, new_position):
        self.squares[old_position[0]][old_position[1]].piece = None
        self.squares[new_position[0]][new_position[1]].piece = piece
        piece.moved = True

    