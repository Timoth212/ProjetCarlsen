
from const import *
from square import Square
from dragger import Dragger
from piece import *

class Board:
    '''
    Il s'agit de l'echiquier mathématique
    '''

#Création du jeu    
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(cols)] #Creation des cases de l'équiquier
        self.dragger = Dragger()
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
            self.squares[row_pawns][col].piece.update_position((row_pawns,col))

        #Knights
        self.squares [row_others][1] = Square(row_pawns,1, Knight(color))
        self.squares[row_others][1].piece.update_position((row_others,1))

        self.squares [row_others][6] = Square(row_pawns,6, Knight(color))
        self.squares[row_others][6].piece.update_position((row_others,6))

        #Bishops
        self.squares [row_others][2] = Square(row_pawns,2, Bishop(color))
        self.squares[row_others][2].piece.update_position((row_others,2))

        self.squares [row_others][5] = Square(row_pawns,5, Bishop(color))
        self.squares[row_others][5].piece.update_position((row_others,5))

        #Rooks
        self.squares [row_others][0] = Square(row_pawns,0, Rook(color))
        self.squares[row_others][0].piece.update_position((row_others,0))

        self.squares [row_others][7] = Square(row_pawns,7, Rook(color))
        self.squares[row_others][7].piece.update_position((row_others,7))

        #Queen
        self.squares [row_others][3] = Square(row_pawns,5, Queen(color))
        self.squares[row_others][3].piece.update_position((row_others,3))

        #King
        self.squares [row_others][4] = Square(row_pawns,4, King(color))
        self.squares[row_others][4].piece.update_position((row_others,4))

# Evolution du jeu       
    def new_piece_position(self, piece, old_position, new_position):
        #modif des placement
        self.squares[old_position[0]][old_position[1]].piece = None
        self.squares[new_position[0]][new_position[1]].piece = piece

        #update des constantes de la piece
        piece.moved = True
        piece.update_position(new_position)

        #est ce qu'il y'a echec?
        ennemy_color = 'black' if piece.color == 'white' else 'white'
        self.is_checked(ennemy_color)
        self.is_checked(piece.color)

        #deplacement roque
        if piece.name =='king' and (new_position[1]-old_position[1]>1):#Si le roi a roque côté droit
            self.new_piece_position(self.squares[old_position[0]][7].piece,[old_position[0],7],[old_position[0],5])

        if piece.name == 'king' and (new_position[1]-old_position[1]<-1): #Si le roi a roque côté gauche
            self.new_piece_position(self.squares[old_position[0]][0].piece,[old_position[0],0],[old_position[0],3])


        #promotion
        '''if piece.name == 'pawn' and (new_position[0] == 0 or new_position[0] == 7) : 
            print("attention...")
            piece.promote()'''

    def ennemy_possible_next_moves(self, mycolor):       
        moves =[]

        for row in range(0,8):
            for col in range(0,8):
                sel_piece = self.squares[row][col].piece
                if sel_piece != None and sel_piece.color != mycolor and sel_piece.name != 'king':
                    sel_piece.possible_moves(self)
                    moves.extend(sel_piece.moves)
        return moves

    def is_checked(self, mycolor):
        """
        Vérifie si le roi de `mycolor` est en échec et met `ischecked = False` si ce n'est pas le cas.
        """

        king = None

        # Trouver la position du roi
        for row in range(8):
            for col in range(8):
                piece = self.squares[row][col].piece
                if piece is not None and piece.color == mycolor and piece.name == 'king':
                    king = piece  # Stocker l'objet roi
                    king_position = (row, col)
        
        king.ischeck = False

        # Vérifier si un coup adverse attaque le roi
        for move in self.ennemy_possible_next_moves(mycolor):
            if move == king_position:  # Si le roi est en danger
                king.ischeck = True
                #self.is_checkmate(king)            

    '''
    def is_checkmate(self,piece):
        if piece.possible_moves(self) == []:
            print("checkmate !")
            '''

